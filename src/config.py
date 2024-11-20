import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    NEYNAR_API_KEY = os.getenv('NEYNAR_API_KEY')
    TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
    TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
    
    # Farcaster Config
    FC_ACCOUNT_MNEMONIC = os.getenv('FC_ACCOUNT_MNEMONIC')
    
    # Posting Schedule
    POST_FREQUENCY = int(os.getenv('POST_FREQUENCY', '4'))  # posts per day
    
    # Data Paths
    DATA_DIR = 'data'
    TRAINING_DATA_PATH = os.path.join(DATA_DIR, 'training_data')
    MODEL_PATH = os.path.join(DATA_DIR, 'model')
