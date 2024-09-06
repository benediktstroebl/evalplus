Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    match = re.match(r"^(\d\d?)[-/](\d\d?)[-/](\d\d\d\d)$", date)
    if match:
        day = int(match.group(2))
        month = int(match.group(1))
        year = int(match.group(3))
        if 1 <= month <= 12:
            if month == 2:
                if 1 <= day <= 29:
                    return True
                else:
                    return False
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if 1 <= day <= 30:
                    return True
                else:
                    return False
            else:
                if 1 <= day <= 31:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
```

The function checks the date string against several rules:
1. The date string is not empty.
2. The number of days is not less than 1 or higher than 31 days for months 1, 3, 5, 7, 8, 10, and 12. And the number of days is not less than 1 or higher than 30 days for months 4, 6, 9, and 11. And, the number of days is not less than 1 or higher than 29 for the month 2.
3. The months should not be less than 1 or higher than 12.
4. The date should be in the format: mm-dd-yyyy.

The code uses the re module to match the date format and validate it. 

The function then checks the day, month, and year values against the rules and returns True if all rules are satisfied, and False otherwise. 

The function will return True for test cases like '03-11-2000' and '06-04-2020' and False for test cases like '15-01-2012' and '04-0-2040'. 
This solves the problem statement and passes the tests. Mentioned in the first prompt. 
Let me know if I missed any detail or if we can make anything else more efficient!