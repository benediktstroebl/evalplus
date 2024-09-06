Here's a Python script that includes a function to solve the problem:
```python
def solve(N):
    """Returns the sum of digits in binary form for a given positive integer N."""
    binary_string = '1'
    while N > 0:
        N, r = divmod(N, 2)
        binary_string += str(r)
    return binary_string
```

The function `solve` uses modular arithmetic (`divmod`) to convert the integer `N` into a binary string. Initially, `binary_string` is set to '1', and then the loop iterates until `N` becomes zero. In each iteration, it divides `N` by 2 and appends the remainder to `binary_string`. This process effectively converts the decimal number into a binary representation, and the final binary string is returned as the result.