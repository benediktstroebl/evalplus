Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string of the sum of its digits.
    """
    total_sum = sum(map(int, str(n)))
    return format(total_sum, 'b')
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits. It converts the integer to a string, sums up the digits, and then converts the result to a binary string using the `format` function with a binary format ('b'). Finally, it returns the binary string representing the sum of the digits in binary format.