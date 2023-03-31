# ChatGPT Telegram Bot for Gophish

ChatGPT Telegram Bot integrates with GoPhish  to simulate phishing attacks and evaluate the preparedness of employees. 

Also the bot is integrated with OpenAI ChatGPT API and after user authorization in Gophish login form with any credantials the bot is capable of generating natural language responses to messages sent by users.

## Prerequisites

Before getting started, you will need to have the following:

 - A Telegram account
 - A Telegram bot token
 - OpenAI API token
 - Python 3.9 or higher

## Installing

1. Clone the repository:

```
git clone https://github.com/dmarushkin/chatgpt-telegram-bot.git

```

2. Install the required Python packages:

```
pip install -r requirements.txt
```

3. Replace TELEGRAM_BOT_TOKEN, OpenAI API Token and other variables in code with relevant for you

4. Install the required Python packages:

```
pip install -r requirements.txt
```

## Running the Bot

1. Run the bot using the following command:

```
python3 telegram_bot.py
```

2. Run the callback webserver using the following command:

```
python3 webserver.py
```

## How it Works

1. Start bot session a with link https://t.me/your_bot_name?start=<rid_code_from_gophish>.

2. Authorize your chat session by following link http://webserver:8000/success?chat_id=<chat_id_from_start_link>

3. Try to ask ChatGPT with command: /gpt Your question


## Contributing

Contributions are always welcome! If you have any suggestions or improvements, please create a pull request.