# One touch Den-Poh

This is notification system using LINE Notify and Raspberry Pi.
The notification.py is the code to execute on Raspberry Pi. The system should be connecting to internet.

![](https://img.shields.io/github/languages/code-size/khiz125/notification_with_raspberry_pi)
![](https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=plastic)

## Features

This code set 2 buttons for message.
To set your text in "message" variables on line 39 and 52, which are currently `"Red button pushed!!"` or `"Blue button pushed!!"`, pushing button on the Raspberry Pi sends message to the LINE notify token account.

# Requirement

## LINE Notify

You need to set LINE Notify token in .env file.
```
LINE_NOTIFY_TOKEN=<Your token here>
```

https://notify-bot.line.me/ja/
![LINE Notify](https://user-images.githubusercontent.com/88763635/187067781-43e05bfa-ada6-4949-be42-194deffaef31.png)

## Tools for Raspberry Pi
![tools](https://user-images.githubusercontent.com/88763635/187067591-0f6cbc53-b107-4581-9d26-9c5bc3edfe18.png)

## Electronics setting (example)
![electronics](https://user-images.githubusercontent.com/88763635/187067697-37e09cf9-d67b-4aac-8c4e-49d01e766311.png)
