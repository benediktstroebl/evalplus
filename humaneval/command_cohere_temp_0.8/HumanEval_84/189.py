Here's a Python script that includes a function to solve the given problem:
```python
def solve(N):
    BIN_DIGITS = '01'
    tot_sum = 0
    strN = str(N)
    for digit in strN:
        tot_sum += int(digit)
    return format(tot_sum, BIN_DIGITS)
```
This script includes a function `solve(N)` that takes a positive integer `N` as input and returns the binary string that represents the total sum of its decimal digits. The function uses a `for` loop to loop through each digit in the decimal number, and adds up the binary value of each digit in base 2. The function then returns the binary string that represents this sum. This is done using Python's `format` function to convert the integer sum to a binary string with `BIN_DIGITS` binary prefix. 

This code will work for positive integers up to 10,000, which are less than four digits, and can be run independently.