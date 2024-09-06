Here's a Python script that contains a function which solves the given problem and is coherent with your introduction:
```python
def solve(n):
    s = str(n)
    return ''.join([str(int(s[i:i+1]) ^ 1) for i in range(len(s))])
```
The function `solve(n)` takes a positive integer `n` as its argument and aims to calculate the sum of its digits in binary. It does so by first converting the integer to a string, `s`. Then, it iterates through the string, converting each digit to its binary counterpart, with the XOR of the digit and 1, to ensure the result is binary. The resulting binary digits are concatenated to form the final binary string representation of the sum.