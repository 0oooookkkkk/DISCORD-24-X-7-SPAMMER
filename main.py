from webserver import keep_alive
import requests

channelID = 982997839187685386
headers = {
    "authorization":
    "ODEyMzQyODAzMjE2NTk3MDQ0.GbTUUG.EekkvllaHDpzfT4i5IfI3bTcOhjL8vByPN5bKw"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
