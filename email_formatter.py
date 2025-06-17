# email_formatter.py

# Simple contact email formatter script
contacts = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"}
]

def format_email(contact):
    return f"""Dear {contact['name']},

This is a friendly reminder that your profile update is due.
Please log in to the system to complete the process.

Best regards,  
Sunil Puri
"""

for contact in contacts:
    print(f"To: {contact['email']}")
    print(format_email(contact))
    print("="*40)
