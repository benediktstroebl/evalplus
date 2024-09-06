Here's a Python script that contains a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary
    :type n: int
    :return: Binary string of the sum of digits in base 10
    :rtype: str
    """
    bin_sum = bin(sum([int(d) for d in str(n)]))[2:]
    return bin_sum if bin_sum.isdigit() else '0' + bin_sum
```

This script defines a function `solve(n)` that takes in a number `n` as an argument and calculates the sum of its digits in base 10. It converts the input into a string, casts it to an integer to autopropely convert it to base 10, and calculates the sum of its digits. The sum is then converted to a binary string and returned. If the binary string only contains digits, it is returned directly, otherwise, it is prepended with a '0' to ensure a valid binary number representation as a string.

The function is designed to handle the given constraints of `0 ≤ N ≤ 10000` and provides the correct binary output for the examples mentioned in the problem statement.