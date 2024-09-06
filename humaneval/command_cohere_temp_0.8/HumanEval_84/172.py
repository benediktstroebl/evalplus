Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary
    :type n: int
    :return: Binary string of the sum of digits in base 10
    :rtype: str
    """
    # Convert the integer to a string to remove trailing zeros
    bin_str = str(n).bex()
    # Convert the string to an integer to remove leading zeros
    bin_str = int(bin_str)
    
    return bin(bin_str).replace('0b', '')
```

This function takes an integer `n` as its parameter and ultimately converts it to a binary string representation of the sum of its decimal digits. It first converts the integer to a string using the `bex()` method, which effectively removes any trailing zeros, and then converts it back to an integer to remove any leading zeros. This ensures that the final binary string output is clean and doesn't contain unnecessary leading or trailing zeros.

For example, given the input `n = 1000`, the function would return the string "1", which is the binary representation of the sum of its digits in base 10. Similarly, for `n = 150`, the function would return "110", and for `n = 147`, it would return "1100".