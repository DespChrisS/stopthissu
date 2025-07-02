import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

TARGET_USER_ID = 947843978861105182, 667668027109670932
YOUR_USER_ID = 1230904729731727460

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot connected as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot or message.guild is None:
        return

    if message.author.id == TARGET_USER_ID:
        try:
            user = await client.fetch_user(YOUR_USER_ID)

            guild_id = message.guild.id
            channel_id = message.channel.id
            message_id = message.id
            message_link = f"https://discord.com/channels/{guild_id}/{channel_id}/{message_id}"

            dm_content = (
                f"📨 **{message.author.name} said in #{message.channel.name}:**\n"
                f"> {message.content}\n"
                f"🔗 [Jump to Message]({message_link})"
            )

            await user.send(dm_content)
            print(f"📬 Forwarded message from {message.author.name} to your DM.")

        except Exception as e:
            print(f"❌ Failed to send DM: {e}")

client.run(TOKEN)
