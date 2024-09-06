Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary
    :type n: int
    :return: Binary string sum of digits of N
    :rtype: str
    """
    # Your code here!
    bin_n = bin(n).replace("0b", "")
    return bin_n if len(bin_n) == 1 else bin_n[:1]
```

This function takes an integer N as input and returns the binary string that sums up the digits of N, using the `bin` function to convert the integer to a binary string and then removing the '0b' prefix added by `bin`. It handles the case where the binary representation of the number has only one digit (e.g. 147 becomes "111001" in binary) by removing the first character to ensure a leading '1' is preserved.