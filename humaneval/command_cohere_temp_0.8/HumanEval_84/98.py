Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String binary representation of the sum of digits of n
    """
    total_sum = 0
    num = str(n)
    for digit in num:
        total_sum += int(digit)
    return format(total_sum, 'b')
```

This function takes an integer `n` as input and iterates through its digits. It converts the integer to a string to easily iterate through its digits, and a loop adds each digit to a running total. After summing the digits, the function converts the total to a binary string and returns it. The binary string represents the sum of the digits of `n` in binary format.