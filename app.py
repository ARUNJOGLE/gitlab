import random
from datetime import datetime

quotes = [
    "Commit 1.1"
    "Believe you can and you're halfway there.",
    "Keep going. Everything you need will come to you at the perfect time.",
    "You are capable of amazing things.",
    "Dream big and dare to fail.",
    "The harder you work for something, the greater you’ll feel when you achieve it."
]

def show_random_quote():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quote = random.choice(quotes)
    print(f"[{now}] 🌟 Quote of the Moment:")
    print(f"➤ {quote}")

if __name__ == "__main__":
    show_random_quote()
