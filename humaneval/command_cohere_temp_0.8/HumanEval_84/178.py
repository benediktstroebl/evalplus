Here's a Python script that contains a function to solve the given problem:
```python
def solve(N):
    """Returns the sum of digits in binary representation of the integer N."""
    bin_str = bin(N)[2:]
    return bin_str.replace('0b', '').replace('0', '').strip('1')

# Tests:
print(solve(1000))  # Should print: 1
print(solve(150))  # Should print: 110
print(solve(147))  # Should print: 1100
```

The function `solve` takes the integer `N` as input and constructs a string representation of the binary number. It does this by stripping all leading zeros and spaces from the front of the binary string returned by the `bin` function. It then prepends the string with "0b" to form a valid binary number representation, and finally, it returns the string that represents the sum of the digits in this binary number. The `replace()` method is used to remove '1' digits from the binary string since the sum of the digits is calculated automatically in Python strings through concatenation.