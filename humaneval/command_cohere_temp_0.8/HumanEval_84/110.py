Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return bin(int(''.join(s))).replace('0b', '')
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It converts the integer to a string, then joins the characters of the string into a longer string, and converts it to an integer. Finally, it converts the result to a binary string and returns it.