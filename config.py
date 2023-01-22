import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21927988")

API_HASH = os.environ.get("API_HASH", "e18f720acdff1e5b0ec80616aecd8a5a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "theoneandonlymurim") 

DB_NAME = os.environ.get("DB_NAME","Ciel")     

ORMONGO_RS_URL = os.environ.get("ORMONGO_RS_URL","")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/8713332eff3b75c095754.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get('PORT', '8080')
