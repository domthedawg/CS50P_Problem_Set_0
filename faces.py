def main():
    text = input("").strip()
    message = convert(text)
    print(message)

def convert(text):
    emoji_replace = text.replace(":)", "🙂").replace(":(", "🙁")
    return emoji_replace



main()