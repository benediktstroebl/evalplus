Here's a Python script that includes a function to solve the problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: Binary string of the sum of the digits of the passed integer
    """
    bin_sum = bin(sum([int(d) for d in str(n)]))[2:]
    return bin_sum if bin_sum.isdigit() else '0' + bin_sum
```

This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary representation. It converts the integer to a string, casts it to binary using `bin`, and extracts the binary representation of the sum using `str[2:]`. If the resulting string is entirely numeric, it is returned as is; otherwise, a '0' is prepended to ensure a valid binary number representation. This approach handles cases where the input integer may not be a multiple of 4, ensuring that the binary sum is correctly formatted with leading zeros as needed.