import discord
from discord.ext import commands, tasks
import datetime
import json
import random
from pytz import timezone
from dotenv import load_dotenv
import os

load_dotenv()

int_bot_token = os.getenv('BOT_TOKEN')
int_guild_id = int(os.getenv('GUILD_ID'))
int_channel_id = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

def load_posts():
    try:
        with open('posts.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def load_messages():
    try:
        with open('messages.json', 'r') as file:
            messages = json.load(file)
    except FileNotFoundError:
        messages = ["Default message without {current_post_count}"]
    return messages

def save_posts(data):
    with open('posts.json', 'w') as file:
        json.dump(data, file, indent=4)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@tasks.loop(hours=24)  # Set the loop to check every 24 hours
async def daily_message():
    gmt = timezone('GMT')
    now = datetime.datetime.now(gmt).date()
    
    target_date = datetime.datetime(now.year, 2, 4, 8, 0, 0, tzinfo=gmt)  # 4th February at 8:00 AM GMT

    if now == target_date.date():
        guild_id = int_guild_id
        channel_id = int_channel_id

        guild = bot.get_guild(guild_id)
        channel = guild.get_channel(channel_id)

        posts = load_posts()
        current_post_count = posts.get('count', 0) + 1
        posts['count'] = current_post_count
        save_posts(posts)

        messages = load_messages()
        selected_message = random.choice(messages).format(current_post_count)
        
        await channel.send(selected_message)

@daily_message.before_loop
async def before():
    await bot.wait_until_ready()

daily_message.start()
bot.run(int_bot_token)