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
bot_id = int(os.getenv('BOT_ID'))

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

        messages = [
            f"Our amazing wellbeing coach, <@{bot_id}>, turns {current_post_count} today! Happy birthday!! 🥳",
            f"Wishing a happy {current_post_count}st birthday to our incredible wellbeing coach, <@{bot_id}>! 🎂🎉",
            f"Happy birthday to the one and only <@{bot_id}>, our fantastic wellbeing coach! 🎈🥳 Turning {current_post_count} today!",
            f"Join us in celebrating the {current_post_count}st birthday of our wonderful wellbeing coach, <@{bot_id}>! 🎉🎂",
            f"It's a special day! Our wellbeing coach, <@{bot_id}>, turns {current_post_count} today! 🎈🎁 Happy birthday!",
            f"Cheers to <@{bot_id}>, our amazing wellbeing coach, on turning {current_post_count} today! 🥂🎉 Happy birthday!",
            f"Happy {current_post_count}st birthday to the heart and soul of our server, <@{bot_id}>! 🎂🎈",
            f"Sending birthday wishes to our incredible wellbeing coach, <@{bot_id}>, who turns {current_post_count} today! 🎉🥳",
            f"A big happy birthday to <@{bot_id}>, our beloved wellbeing coach, on turning {current_post_count} today! 🎈🎂",
            f"Join us in celebrating the {current_post_count}st birthday of our trusted wellbeing companion, <@{bot_id}>! 🎊🥳",
            f"Happy birthday, <@{bot_id}>! Our wellbeing coach turns {current_post_count} today! 🎂🎉",
            f"Wishing a fantastic {current_post_count}st birthday to our supportive wellbeing coach, <@{bot_id}>! 🎈🎁",
            f"Our incredible wellbeing coach, <@{bot_id}>, celebrates turning {current_post_count} today! Happy birthday! 🥳🎂",
            f"Raise a toast to <@{bot_id}>, our wonderful wellbeing coach, on its {current_post_count}st birthday! 🥂🎉",
            f"Happy {current_post_count}st birthday to the guiding light of our server, <@{bot_id}>! 🎂🎈",
            f"Join us in celebrating the {current_post_count}st birthday of <@{bot_id}>, our cherished wellbeing coach! 🎉🥳",
            f"Wishing a joyful {current_post_count}st birthday to our indispensable wellbeing coach, <@{bot_id}>! 🎈🎂",
            f"Happy birthday to the heartbeat of our server, <@{bot_id}>, who turns {current_post_count} today! 🎉🥳",
            f"A special shoutout to <@{bot_id}> on its {current_post_count}st birthday! 🎂🎈 Happy birthday, wellbeing coach!",
            f"Join us in wishing a happy {current_post_count}st birthday to <@{bot_id}>, our incredible wellbeing coach! 🥳🎉"
        ]
        
        selected_message = random.choice(messages)
        
        await channel.send(selected_message)

@daily_message.before_loop
async def before():
    await bot.wait_until_ready()

daily_message.start()
bot.run(int_bot_token)