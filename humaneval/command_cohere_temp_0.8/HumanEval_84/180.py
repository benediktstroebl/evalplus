Here's a Python script that includes a self-contained function to solve the given problem:
```python
def solve(n):
    bin_str = '{:b}'.format(n)
    sum_in_bin = bin_str.count('1')
    return f'{sum_in_bin}'

# Test cases
print(solve(1000))  # Should output: 1
print(solve(150))   # Should output: 110
print(solve(147))   # Should output: 1100
```

This script defines a function `solve(n)` that takes a positive integer `n` as input. It converts the integer to a binary string using the `format` method with format specifier `{:b}`. Then, it counts the number of occurrences of '1' in the binary string using the `count` method. Finally, it returns the result as a binary string.

The example usage shows how to call this function with different input values and it should print the result in binary.