Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be transformed to binary and have its digits summed
    :return: Binary string summation of integer
    """
    bin_n = bin(n).replace("0b", "")
    return bin_n if len(bin_n) <= 8 else bin_n[0:8]
```

This function takes an integer `n` and transforms it into a binary string, and then returns the binary string whose length is at most 8 characters, if it's longer than this length. It does this to ensure that the sum of the digits in binary form gives the desired integer `n`.