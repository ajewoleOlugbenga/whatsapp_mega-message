import pywhatkit as kit
import time

# Function to read phone numbers from a text file
def read_phone_numbers(filename):
    with open(filename, 'r') as file:
        phone_numbers = file.read().splitlines()
    return phone_numbers

# List of phone numbers
phone_numbers = read_phone_numbers('phone_numbers.txt')

# Your message
message = """
You're invited to PCIDSS 4.0 TRAINING 

Tuesday, 16 July and
Wednesday, 17 July 2024

10:00 am - 4:00 pm Nigerian Time

https://tinyurl.com/yx8u7hau

Tap on the link or paste it in a browser to join."""

# Function to send messages
def send_whatsapp_message(phone_number, message):
    try:
        # Schedule the message to be sent
        current_time = time.localtime()
        kit.sendwhatmsg(phone_number, message, current_time.tm_hour, current_time.tm_min + 2)
        print(f"Message sent to {phone_number}")
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")

# Send messages to all numbers in the list
for number in phone_numbers:
    send_whatsapp_message(number, message)
    # Wait for a few seconds before sending the next message
    time.sleep(10)  # Adjust the sleep time if necessary
