Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String binary representation of the sum of digits of n
    """
    total_sum = 0
    num = str(n)
    while len(num) > 0:
        total_sum += int(num[0])
        num = num[1:]
        num = str(int(num) + num)
    return format(total_sum, 'b')
```

This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It converts the integer to a string, iterates through each digit, and accumulates the sum of the digits in binary. The binary sum is then returned as a string.