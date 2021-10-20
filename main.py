import imports
from imports import *
client= utils.bot

@client.event
async def on_ready():
    print(f"{client.user} is alive\nis nice")

# Put everything before this command and don't share the token with anybody
client.run(utils.token)
