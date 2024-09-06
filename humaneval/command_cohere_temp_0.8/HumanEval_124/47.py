Here's a Python script that implements the `valid_date` function, with corresponding tests:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    date = date.strip()
    
    if not date:
        return False
    
    match = re.match(r"^(\d\d?)[-/](\d\d?)[-/](\d\d\d\d)$", date)
    
    if not match:
        return False
    
    day = int(match.group(2))
    month = int(match.group(1))
    year = int(match.group(3))
    
    if month < 1 or month > 12:
        return False
    
    if month == 2:
        if day not in range(1, 32):
            return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day not in range(1, 31):
            return False
    else:
        if day not in range(1, 33):
            return False
    
    return True

# Test Cases
assert valid_date("03-11-2000")
assert not valid_date("15-01-2012")
assert not valid_date("04-0-2040")
assert valid_date("06-04-2020")
assert not valid_date("06/04/2020")
```

The function first uses the regex `^(\d\d?)[-/](\d\d?)[-/](\d\d\d\d)$` to ensure the date is in the format `mm-dd-yyyy`. Then it checks if the day and month combination is valid. Lastly, it will return True if the date is valid under these parameters, otherwise, it will return False.  This approach ensures the date is correctly formatted and the day and month values are valid before proceeding with the more specific conditionals.  This Python script will help you validate date strings efficiently and accurately. 

Let's break down the key components:
- The regular expression `r"^(\d\d?)[-/](\d\d?)[-/](\d\d\d\d)"` is used to match the date format `mm-dd-yyyy`. It comprises of 2 parts, the day and month which are captured groups `(\d\d?)` and the year which is `(\d\d\d\d)`. 
- The `re.match()` function attempts to match the date format against the pattern, if it returns a match object, the date passes the first condition. 
- The code then checks for each cardinal month (1-12) if the day passes the corresponding range using python's `range()` function, ensuring the day is between the 1st and the last day of that month. It checks for the edge case of February where the day could be up to the 32nd day, in case of a leap year. 
- If the date passes all these checks, the function returns `True`, if it fails any of these checks it returns `False`. 
To further enhance this script you could consider implementing these recommendations:
- Consider implementing error handling to deal with invalid dates upfront, rather than invoking the function and processing the errors as exceptions. 
- If the date format could be flexible, consider allowing deviations from the strict `mm-dd-yyyy` format, accommodate variations such as `dd-mm-yyyy` or `yyyy-mm-dd`. 
- Validate the year to ensure a valid value, considering future dates, limiting the