# Discord Anniversary Bot

Welcome to the Discord Anniversary Bot! This bot is designed to send automated anniversary messages on a specific date each year.

## Features

- Sends a customised anniversary message on the 4th of February each year at 8:00 AM GMT.
- The message includes a mention of the bot using its Discord ID and the current post count (birthday).
- Randomly selects a message from a predefined list for added variety.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Discord account and a bot token

### Installation

1. Clone the repository:

git clone https://github.com/garybpt/discord-anniversary-bot.git

2. Install the required packages:

pip install -r requirements.txt

### Configuration

1. Create a .env file in the project root and add your bot token, guild ID (server), channel ID, and bot ID:

BOT_TOKEN=your_bot_token_here
GUILD_ID=your_guild_id_here
CHANNEL_ID=your_channel_id_here
BOT_ID=your_bot_id_here

2. Customise the messages list in the Python script with your preferred anniversary messages.

### Running the Bot

Run the bot using the following command:

python ana_ai_birthday.py

The bot will start and automatically send anniversary messages on the specified date.

### Customization

Feel free to customise the bot further by modifying the code, changing the anniversary messages, or adding new features.

### Contributing

If you'd like to contribute to this project, fork the repository and submit a pull request.

### License

This project is licensed under the MIT License.