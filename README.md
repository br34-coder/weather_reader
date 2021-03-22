# weather_reader
Little playground to read data from my weather station and post it via telegram messenger

## How to init the telegram sender
This section describes how to create a bot in telegram and use it to send messages via python

### Create the bot
1. Open the telegram app on your smartphone and search for @BotFather
2. Press the start button
3. Send "/newbot", create a name and username
4. Note down the API token provided

### Prepare telegram-send
1. Install telegram-send: `pip3 install telegram-send`
2. Configure telegram-send: `telegram-send --configure`
3. The config tool will now ask you for the token you got from the BotFather, ask you to add him on your telegram App and send a password given.

### Send messages using python
Once the preps have been done, its straight forward:
```python
import telegram_send
telegram_send.send(messages=["Hello World!"])
``` 
