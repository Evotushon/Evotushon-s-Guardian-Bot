import imports
from imports import *
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# Prefisso cambiabile in ogni momento
prefix = "ev! "
bot = commands.Bot(command_prefix=prefix)
token = TOKEN

