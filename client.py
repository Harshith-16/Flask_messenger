import requests
# import requests

BASE_URL = 'http://localhost:5000'  # Change if your server runs on a different port or host

def send_message(content):
    response = requests.post(f'{BASE_URL}/send_message', json={'content': content})
    return response.json()

def get_messages():
    response = requests.get(f'{BASE_URL}/get_messages')
    return response.json()

if __name__ == '__main__':
    login = True
    while login:
        print("1. Send Message")
        print("2. Get Messages")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            content = input("Enter message content: ")
            result = send_message(content)
            print(result)
        elif choice == '2':
            messages = get_messages()
            for message in messages['messages']:
                print(f"Message ID: {message['id']}, Content: {message['content']}")
        elif choice == '3':
            login = False
            print("Program Exited!")
        else:
            print("Invalid choice")
