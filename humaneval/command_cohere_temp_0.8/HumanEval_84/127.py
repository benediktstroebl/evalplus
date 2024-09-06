Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    s = str(n)
    return bin(sum(int(d) for d in s))[2:].zfill(len(s))
```
This script defines a function `solve(n)` that takes an integer `n` as input and calculates the sum of its digits in binary. It converts the integer to a string `s`, and then uses a generator expression to sum the digits converted to integers. The result is converted to a binary string and padded with leading zeros (using `zfill`) to match the length of the original number's string representation, ensuring a binary representation without leading zeros.