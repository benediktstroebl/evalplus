Here's a Python script that includes a function to solve the given problem:
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

This function takes an integer n as input and calculates the sum of its digits in base 10. It converts the integer to a string, extracts the digits, sums them up, and then converts the sum into a binary string. If the binary string only contains zeros and ones (i.e., it's a valid binary number), it's returned as is; otherwise, a prefix of '0' is added to make it valid. This way, the function always returns a string representing the binary value of the sum of the digits.

For example, given the input `n = 1000`, the function would return `"1"` as the sum of its digit in binary is 1; For `n = 150`, the function would return `"110"`; For `n = 147`, the function would return `"1101110"` respectively.