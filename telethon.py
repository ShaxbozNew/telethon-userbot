import os
try:
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types
except:
    os.system('pip install telethon')
    from telethon.sync import TelegramClient
    from telethon import TelegramClient,events,sync
    from telethon import functions,types

bot = input("Shaxboz")
api_id = 10279988
api_hash = "cc10c52f2706c2e5969b366e3cab421c"
client = TelegramClient(bot,api_id,api_hash)
client.start()
@client.on(events.NewMessage)
async def my_event_handler(event):
    if event.raw_text == ".salom":
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵\n🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵")
        await event.edit("🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴\n🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴")
        await event.edit("Salom hammaga ")
    elif event.raw_text == ".b":
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️⬜️◻️⬜️◻️⬜️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n⬜️◻️⬜️◻️⬜️◼️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️◼️⬜️◻️⬜️◻️⬜️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️⬜️◻️⬜️◻️⬜️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n⬜️◻️⬜️◻️⬜️◼️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️◼️⬜️◻️⬜️◻️⬜️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️⬜️◻️⬜️◻️⬜️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n⬜️◻️⬜️◻️⬜️◼️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️◼️⬜️◻️⬜️◻️⬜️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️⬜️◻️⬜️◻️⬜️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n⬜️◻️⬜️◻️⬜️◼️◼️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit("◼️◼️◼️◼️◼️◼️◼️\n◼️◼️◼️😜◼️◼️◼️\n◼️◼️⬜️◻️⬜️◻️⬜️\n◼️◼️◼️⬜️◼️◼️◼️\n◼️◼️⬜️◻️⬜️◼️◼️\n◼️◼️◻️◼️◻️◼️◼️")
        await event.edit(" Nima gaplar")


client.run_until_disconnected()




#Remember api_id Is int and no need to put "" or ''
#Remember api_hash Is string and need to put " in first and end it
#find another Commands and requests from tl.telethon.dev
