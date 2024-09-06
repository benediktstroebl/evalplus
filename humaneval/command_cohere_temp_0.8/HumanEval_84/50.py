Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    """Returns the sum of digits in binary representation of the given integer n."""
    bin_str = bin(n)[2:]
    return bin_str.count('1')

# Test cases
print(solve(1000))  # Output: 1
print(solve(150))  # Output: 110
print(solve(147))  # Output: 1100
```
This script includes the solve function and provides example test cases to verify its correctness. The function simply converts the integer to a binary string, excluding the leading '0b', and then counts the number of '1's in the string to obtain the sum of the digits in binary representation.