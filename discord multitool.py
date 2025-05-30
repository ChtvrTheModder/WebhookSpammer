import os 
import time
import requests
import sys
import webbrowser


def send_webhook():
    webhook_url = input("Enter Webhook URL:\n").strip()
    message = input("Enter the message you want to spam:\n").strip()
    count = int(input("How many messages do you want to send?\n"))

    payload = {
        "content": message  
    }

    for i in range(count):
        try:
            time.sleep(1)
            response = requests.post(webhook_url, json=payload)
            if response.status_code in [200, 204]:
                print(f"Sent message #{i+1}")
            else:
                print(f"Failed to send webhook. Status code: {response.status_code}")
                print("Response:", response.text)
        except Exception as e:
            print(f"Error: {e}")

def open_discord_server():
    print("Opening Discord server link...")
    webbrowser.open("https://discord.gg/4u9gRrTxZb")


def Main_menu():
    while True:  
        print("\nWelcome to my Discord multitool")
        print("1. Webhook spammer")
        print("2. Our Discord server")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            send_webhook()
        elif choice == "2":
            open_discord_server()  
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

Main_menu()
