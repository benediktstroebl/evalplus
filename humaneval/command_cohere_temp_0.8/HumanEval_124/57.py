Here's a Python script that defines a function to validate a date string based on the provided rules:
```python
import re

def valid_date(date):
    """
    Validate a given date string and return True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    yyyy, mm, dd = map(int, re.sub(r'[^0-9]', '', date).split('-'))
    
    # Check if the date is valid
    if (mm < 1 or mm > 12) or (dd < 1 or dd > dias_anos[mm] ) or (yyyy < 2000):
        return False
    
    return True

def main():
    print(valid_date('06-04-2020'))  # Should print True
    print(valid_date('06/04/2020'))  # Should print False
    print(valid_date('03-11-2000'))  # Should print True
    print(valid_date('15-01-2012'))  # Should print False
    print(valid_date('04-0-2040'))  # Should print False

dias_anos = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

if __name__ == "__main__":
    main()
```

This script uses regular expressions to validate the date format and checks the validity of the date components (month, day, and year) against the defined rules. The `dias_anos` dictionary provides the maximum days for each month. The script includes a `main` function to run some example tests and prints the validity of the dates. Adjust these tests or add more as needed.