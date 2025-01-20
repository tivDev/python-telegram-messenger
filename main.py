import requests

def send_msg(text, count):
    token = "your_bot_token"
    chat_id = "your_chart_id"
    base_url = "https://api.telegram.org/bot" + token + "/sendMessage"
    
    sent_messages = []  # List to store sent messages' text
    
    for i in range(1, count + 1):
        message = f"Message: {i} - {text}"
        url_req = f"{base_url}?chat_id={chat_id}&text={message}"
        results = requests.get(url_req)
        response = results.json()
        
        # Extract only the 'text' field from the response and append to the list
        if response.get("ok"):
            sent_messages.append(response['result']['text'])
            print(response['result']['text'])
    
    return sent_messages  # Return the list of messages that were sent

send_msg("Hello there! send me a message", 5)
