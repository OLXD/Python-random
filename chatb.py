#!/usr/bin/env python3
print("Let's talk! Enter 'quit' to exit...")

while True:
    user = input("You: ")
    print(f"Bot: {user}")

    if user == 'quit':
        break
