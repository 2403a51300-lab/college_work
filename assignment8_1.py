import string

def is_strong_password(password):
    # Check length
    if len(password) < 8:
        return False
    # Check for spaces
    if " " in password:
        return False
    # Check for uppercase, lowercase, digit, and special character
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    return has_upper and has_lower and has_digit and has_special

# Assert test cases
assert is_strong_password("Abcd@123") == True
assert is_strong_password("abcd123") == False
assert is_strong_password("ABCD@1234") == True
assert is_strong_password("Abc12345") == False
assert is_strong_password("Abcd@ 123") == False


def classify_number(n):
    # Handle invalid inputs
    if not isinstance(n, (int, float)) or n is None:
        return "Invalid input"
    # Loop-based classification (for demonstration)
    for value in [n]:
        if value > 0:
            return "Positive"
        elif value < 0:
            return "Negative"
        else:
            return "Zero"

# Assert test cases
assert classify_number(10) == "Positive"
assert classify_number(-5) == "Negative"
assert classify_number(0) == "Zero"
assert classify_number(-1) == "Negative"
assert classify_number(1) == "Positive"
assert classify_number("abc") == "Invalid input"
assert classify_number(None) == "Invalid input"

import string

def is_anagram(str1, str2):
    # Helper function to clean and normalize strings
    def clean(s):
        # Remove spaces and punctuation, convert to lowercase
        return ''.join(c.lower() for c in s if c.isalnum())
    s1 = clean(str1)
    s2 = clean(str2)
    # Edge case: both empty strings are considered anagrams
    if s1 == "" and s2 == "":
        return True
    # Compare sorted characters
    return sorted(s1) == sorted(s2)

# Assert test cases
assert is_anagram("listen", "silent") == True
assert is_anagram("hello", "world") == False
assert is_anagram("Dormitory", "Dirty Room") == True
assert is_anagram("", "") == True
assert is_anagram("a", "A") == True
assert is_anagram("conversation", "voices rant on") == True
assert is_anagram("test", "ttew") == False


class Inventory:
    def __init__(self):
        # Initialize inventory as an empty dictionary
        self.stock = {}

    def add_item(self, name, quantity):
        # Add quantity to item; create item if it doesn't exist
        if name in self.stock:
            self.stock[name] += quantity
        else:
            self.stock[name] = quantity

    def remove_item(self, name, quantity):
        # Remove quantity from item if it exists and enough stock is available
        if name in self.stock:
            self.stock[name] = max(0, self.stock[name] - quantity)

    def get_stock(self, name):
        # Return current stock for item, or 0 if not found
        return self.stock.get(name, 0)

# Assert-based test cases
inv = Inventory()
inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10
inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5
inv.add_item("Book", 3)
assert inv.get_stock("Book") == 3
inv.remove_item("Book", 5)  # Removing more than available
assert inv.get_stock("Book") == 0
assert inv.get_stock("Pencil") == 0  # Item not in inventory


from datetime import datetime

def validate_and_format_date(date_str):
    # Try to parse the date in MM/DD/YYYY format
    try:
        date_obj = datetime.strptime(date_str, "%m/%d/%Y")
        # If successful, format to YYYY-MM-DD
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        # If parsing fails, it's an invalid date
        return "Invalid Date"

# Assert test cases
assert validate_and_format_date("10/15/2023") == "2023-10-15"
assert validate_and_format_date("02/30/2023") == "Invalid Date"
assert validate_and_format_date("01/01/2024") == "2024-01-01"
assert validate_and_format_date("13/01/2024") == "Invalid Date"  # Invalid month
assert validate_and_format_date("12/31/2022") == "2022-12-31"