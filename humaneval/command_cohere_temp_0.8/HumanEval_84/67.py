Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary
    :return: Binary string sum of digits of n
    """
    bin_str = bin(n)[2:]
    return bin_str.replace('0b', '').replace('0', '').strip()

# Test cases
print(solve(1000) == '1')
print(solve(150) == '110')
print(solve(147) == '1100')
```

The function solve takes an integer n as input and returns the binary string sum of its digits. To get the sum in binary, the function converts the integer to binary and then does the following:
- Removes '0b' from the start of the binary string.
- Replaces all '1's with ''.
- Removes all '0's.
- Strips any trailing whitespace.

This problem can be solved much more elegantly and efficiently in Python, using its built-in functionalities. You can simply use `bin()` to convert to binary and then operate on the resulting string.