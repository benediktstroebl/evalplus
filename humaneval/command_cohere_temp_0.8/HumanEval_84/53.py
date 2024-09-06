Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return ''.join([str(int(s[i:i+1]) ^ 1) for i in range(len(s))])
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the binary digit sum of its digits. It converts the integer to a string, iterates through its digits, and converts each digit to its binary representation by taking its binary complement (XOR with 1), and then joins these binary digits to produce the final binary string representation of the sum.