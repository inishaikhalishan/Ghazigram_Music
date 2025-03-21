from GhazigramMusic.core.bot import bot
from GhazigramMusic.plugins.start import Start



with bot:
    Start()
    
    bot.run_until_disconnected()