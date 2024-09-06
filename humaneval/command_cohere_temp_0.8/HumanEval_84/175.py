Here's a Python script that contains a function which solves the given problem and is able to pass the corresponding tests:
```python
def solve(n):
    """
    :param n: Integer to be transformed to binary string
    :return: Binary string of the sum of digits in base 10
    """
    bin_sum = bin(sum([int(d) for d in str(n)]))[2:]
    return bin_sum if bin_sum.isdigit() else '0' + bin_sum
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in base-10. It converts the input integer `n` to a string, extracts its digits, sums them up, and converts the result back to a binary string. The function returns a binary string that represents the sum of the digits in base-10. This solution works correctly for positive integers up to 10,000.