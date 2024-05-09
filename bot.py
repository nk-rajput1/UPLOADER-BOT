#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | Modifieded By : @DC4_WARRIOR

import os
import logging
from config import Config
from pyrogram import Client as Clinton
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


import os  # Import the os module to work with file system operations
from pyrogram import Client

# Create a Pyrogram Client instance
app = Client("my_session")

# Check if DOWNLOAD_LOCATION directory exists
if not os.path.isdir(Config.DOWNLOAD_LOCATION):
    os.makedirs(Config.DOWNLOAD_LOCATION)  # Create the directory if it doesn't exist

# Define the message handler
@app.on_message()
async def handle_message(client, message):
    print(message)

# Run the Pyrogram Client
if __name__ == '__main__':
    app.run())
    plugins = dict(root="plugins")
    Warrior = Clinton("@BOT_X_BOT",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins)
    Warrior.run()
