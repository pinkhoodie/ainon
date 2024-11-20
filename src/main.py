import schedule
import time
from datetime import datetime
from src.api.farcaster import FarcasterClient
from src.llm.model import LLMHandler
from src.utils.data_collector import DataCollector
from config import Config

class AINon:
    def __init__(self):
        self.fc_client = FarcasterClient()
        self.llm_handler = LLMHandler()
        self.data_collector = DataCollector()
        
    def collect_training_data(self):
        """Collect training data from Farcaster and Twitter"""
        self.data_collector.collect_farcaster_data()
        
    def train_model(self):
        """Finetune the LLM on collected data"""
        self.llm_handler.finetune()
        
    def generate_and_post(self):
        """Generate content and post to platforms"""
        content = self.llm_handler.generate_content()
        self.fc_client.post_cast(content)
        
    def setup_schedule(self):
        """Set up posting schedule"""
        interval = 24 / Config.POST_FREQUENCY
        for hour in range(0, 24, int(interval)):
            schedule.every().day.at(f"{hour:02d}:00").do(self.generate_and_post)

def main():
    ainon = AINon()
    ainon.collect_training_data()
    ainon.train_model()
    ainon.setup_schedule()
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
