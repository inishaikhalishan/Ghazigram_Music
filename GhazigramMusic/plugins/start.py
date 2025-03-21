from telethon.sync import events
from GhazigramMusic.core.bot import bot


class Start:
    @bot.on(events.NewMessage(pattern="/start"))
    async def start(event):
        await event.respond("ma chud gya lund lund zenitsu")