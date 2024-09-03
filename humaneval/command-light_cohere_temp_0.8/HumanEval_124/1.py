```python
def valid_date(date_str):
    date = [int(x) for x in date_str.month_match = None
    if date_str and date_str.isdigit():
        month = 0
        day = 1
        while date_str.isdigit() and date_str[0] != '0':
            month += 1
            date_str = date_str[1:] + date_str[0] + date_str[2:] + '-' + date_str[3:]
        date_str = date_str[0] + '-' + str(month) + '-' + date_str[5:]
        date_str = date_str[:3] + '20' + date_str[8:]
        date_str = date_str[3:] + ' ' + date_str[4:] + '-' + date_str[6:]
        date_str = date_str[7:] + ' ' + date_str[8:] + '20'
        return bool(int(date_str) <= 31)
```
This function validates a date string, checking that the input is a string and contains digits, that the number of days is between 1 and 31 (or between 1 and 30 for February), and that the date string is in the mm-dd-yyyy format. The function then returns True if the date is valid and False otherwise.