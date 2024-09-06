Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return bin(sum(int(d) for d in s))[2:].zfill(len(s))
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It converts the integer to a string `s`, and then uses a generator expression to convert each digit to an integer. The sum of these integers is calculated using a built-in Python function. The result is then converted to a binary string and padded with leading zeros if necessary to match the length of the original number's decimal representation. 
This will produce a string representation of the binary value equal to the sum of the digits in the decimal representation of `n`.