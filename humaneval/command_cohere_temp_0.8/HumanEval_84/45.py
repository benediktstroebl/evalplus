Here's a Python script that includes a function to solve the problem:
```python
def solve(n):
    """Returns the sum of digits in binary representation of the given integer n."""
    bin_str = bin(n)[2:]
    return bin_str.replace('0b', '').replace('0', '').upper()

# Test Cases
print(solve(1000) == '1')
print(solve(150) == '110')
print(solve(147) == '1100')
```

The function `solve` takes an integer `n` as input and returns the sum of its binary digits. To get the binary representation of the number, we use `bin(n)[2:]`. Using methods like `.replace()` and `.upper()`, we remove any leading '0b' and change any individual digits from 0 to 1 to get the sum of digits in binary representation. The example usage demonstrates the function's behavior on different inputs.