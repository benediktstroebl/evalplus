Here's a Python script that contains a function which solves the given problem and is compatible with the stated constraints:
```python
def solve(N):
    """
    Get the sum of digits in binary representation of the given integer N.
    """
    bin_str = bin(N)[2:]
    sum_digits = bin_str.count('1')
    return str(sum_digits)
```
This function uses the built-in `bin` function to convert an integer to a binary string and then removes the leading '0b' and trailing 'l' characters. Then the `count` method is used to count the number of '1's in the binary string, which gives the sum of the digits. The result is returned as a binary string with `str` function.

To manage the constraints, the function assumes that the input integer `N` is already in the range `[0, 10000]`. If the input range is not constrained, you may need additional checks or messaging to guide the user.