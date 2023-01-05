messageList = ["hello", "on my way", "are you there?"]
sentMessages = []
def showMessages(messages):
    """prints messages."""
    for message in messages:
        print(message)

def sendMessages(messages):
    """Simulates sending text message."""
    for message in messages:
        print(f"Sending {message}...")
        sending = messages.pop()
        messages.append(sending)
    print("You sent:")
    for sentMessage in messages:
        print(sentMessage)


    
sendMessages(messageList)
