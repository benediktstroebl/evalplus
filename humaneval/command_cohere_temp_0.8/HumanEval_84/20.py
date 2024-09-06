Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String binary representation of the sum of digits of n
    """
    total_sum = 0
    for digit in str(n):
        total_sum += int(digit)
    return format(total_sum, 'b')
```

This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It initializes a variable `total_sum` to 0, then iterates through each digit in the string representation of `n`, converting each digit to an integer and adding it to `total_sum`. Finally, it returns the binary representation of `total_sum`.