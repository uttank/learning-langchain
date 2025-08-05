import os
from dotenv import load_dotenv
# load .env
load_dotenv()
#api_key test
api_key = os.environ.get("OPENAI_API_KEY")