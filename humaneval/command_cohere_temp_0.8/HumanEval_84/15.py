Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string sum of digits of N
    """
    total_sum = 0
    tmp_n = str(n)
    while tmp_n:
        digit = tmp_n % 10
        total_sum += digit
        tmp_n = tmp_n // 10
    return format(total_sum, 'b')
```

This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It converts the input integer to a string temporarily and iterates through each digit, accumulating the sum of the digits in a variable called `total_sum`. After converting the sum from a decimal number to a binary string, it returns the binary string representation of the total sum of the digits.