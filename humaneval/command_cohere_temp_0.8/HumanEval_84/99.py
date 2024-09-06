Here's a Python script that includes a function to solve the problem:
```python
def solve(n):
    """Returns the sum of digits in binary representation of the given integer n."""
    binary_string = '0' * (len(bin(n)) - 2)
    result = 0
    while n:
        n, r = divmod(n, 2)
        result += r
        binary_string = str(r) + binary_string
    return binary_string + str(result)
```
This code defines a function `solve` taking a single integer `n` as input, it initially creates a binary string of length `len(bin(n)) - 2` to account for the leading '0b' and possible trailing zeros, after that, it enters a loop where it keeps dividing `n` by 2 and adding the remainder to the `result` variable and the equivalent number of bits to the `binary_string`. Finally, it returns the binary string concatenated with the result variable which gives the desired output. This solution adheres to the specified constraints.