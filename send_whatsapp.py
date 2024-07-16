import pywhatkit as kit
import time

# List of phone numbers in the format "+<country_code><phone_number>"
phone_numbers = [
    "+1234567890",
    "+1987654321",
    "+2347031371033",
    "+2348163607401",
    "+2348038803243",
    "+2348143695079",
    "+2348059963789",
    "+2348107649713",
    "+233559928668",
    "+233243065778",
    "+233205793955",
    "+233207388532",
    "+2348133748128",
    "+233205834864",
    "+233504004787",
    "+233201358327",
    "+233263474900",
    "+2348145909912",
    "+233508438801",
    "+2349036286848",
    "+233244749371",
    "+233205548882",
    "+233242131135",
    "+233200203995",
    "+233246988165",
    "+2347040001919",
    "+2348023192506",
    "+233202563974",
    "+2348132956021",
    "+2348069031599",
    "+2347051598561",
    "+2348139173747",
    "+2349074994654",
    "+233596915708",
    "+2349035680981",
    "+2348136123111",
    "+233552528688",
    "+2348132128946",
    "+2348139173747",
    "+233507122102",
    "+233572101774",
    "+233201290965",
    "+233245842458",
    "+233501227352",
    "+233549998196",
    "+233540328982",
    "+233247006642",
    "+233530477792",
    "+237678093330",
    "+2348025560631",
    "+237678093330",
    "+2349032603139",
    "+23320123456789",
    "+2347031475543"
    # Add more numbers here
]

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
