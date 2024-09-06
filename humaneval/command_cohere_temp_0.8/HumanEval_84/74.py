Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    bin_str = bin(n)[2:]
    sum_str = ''.join(str(int(bit) for bit in bin_str if bit == '1'))
    return sum_str
```
This script defines a function `solve(n)` taking an integer `n` as input, it first converts the integer into a binary string (`bin_str`) and removes the leading '0b' prefix. Then, it creates a new string called `sum_str` which concatenates the bits that correspond to digits that are 1 (when converted back to a decimal number). This string is then returned as the sum of the digits in binary representation.

This solution assumes that the input `n` is already validated to be a positive integer within the given range (0 ≤ N ≤ 10000).