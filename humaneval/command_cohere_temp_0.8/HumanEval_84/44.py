Here's a Python script that includes a function to solve the problem:
```python
def solve(N):
    BIN_DIGIT_SUM = ''.join(str(bin(N)[2:]).count('1'))
    return BIN_DIGIT_SUM
```
This script defines a function `solve(N)` that takes in a positive integer `N` as its argument and returns the total sum of its binary digits. The function utilizes the fact that the binary representation of a number can be thought of as a summation of successive binary digits, where each digit is either `0` or `1`. It uses the expression `str(bin(N)[2:]).count('1')` to convert the integer `N` to a binary string, omitting the leading `0b`, and then counts the number of occurrences of `1` in that string. This count produces the desired total sum of binary digits, which is then returned as a binary string.  This function is designed to handle any positive integer `N` within the range of 0 to 10,000.