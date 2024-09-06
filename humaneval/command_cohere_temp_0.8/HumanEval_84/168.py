Here's a Python script that includes a function to solve the problem:
```python
def solve(n):
    s = str(n)
    return ''.join([str(int(s[i:i+1]) ^ 1) for i in range(len(s))])
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the binary digit sum of its digits. It converts the integer to a string and uses a list comprehension to convert each digit to its binary equivalent by taking its complement. The function returns a string of binary digits.