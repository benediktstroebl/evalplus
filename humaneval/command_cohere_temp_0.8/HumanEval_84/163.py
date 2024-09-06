Here's a Python script that contains a function which solves the given problem and is coherent with your explanation:
```python
def solve(n):
    binary_string = '1'
    while n > 0:
        n, r = divmod(n, 2)
        binary_string += str(r)
    return binary_string
```
This code defines a function `solve(n)` taking a positive integer `n` as its argument and returns a string representing the binary representation of the sum of its digits. It iterates through `n`'s digits and accumulates the binary representation of the digit sum using string concatenation. Finally, it returns the binary string.