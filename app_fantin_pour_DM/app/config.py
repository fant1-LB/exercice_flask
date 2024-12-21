import dotenv
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv.load_dotenv(os.path.join('.env'))
def to_bool(s):
    r = False 
    if s == "TRUE":
        r = True
    elif s == "FALSE":
        r = False
    return r
class Config():
    DEBUG = to_bool(os.environ.get("DEBUG"))