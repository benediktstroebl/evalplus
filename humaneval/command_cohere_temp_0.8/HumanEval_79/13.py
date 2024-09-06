Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Returns binary string for given decimal number with extra 'db' chars"""
    res = ''
    while decimal:
        digit = decimal % 2
        res = str(digit) + res
        decimal //= 2
    return 'db' + res + 'db'
```

The function uses a loop to repeatedly divide the input decimal value by 2 and appends a binary digit to the result based on the remainder. The process continues until the input is exhausted, and the result is then prepended and appended with the string 'db' to ensure the desired output format.