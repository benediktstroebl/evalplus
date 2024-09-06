Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return bin(sum(int(d) for d in s))[2:][:len(s)]
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It converts the integer to a string `s`, and then uses a generator expression within the sum function to convert each digit to an integer. Then it converts the resulting binary string to a binary number, right-aligned to match the length of the original number, and returns it as a string.  This aligns with the problem statement's request to return the output as a string of binary digits.