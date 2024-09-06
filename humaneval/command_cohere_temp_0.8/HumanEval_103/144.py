Here's a Python script with a self-contained function `rounded_avg(n, m)` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    binary_representation = bin(round(avg))[2:]
    return binary_representation if binary_representation.isalpha() else '0b' + binary_representation

# Test Cases
print(rounded_avg(1, 5))  # Output: 0b11
print(rounded_avg(7, 5))  # Output: -1
print(rounded_avg(10, 20))  # Output: 0b1111
print(rounded_avg(20, 33))  # Output: 0b11010
```

This code defines a function `rounded_avg(n, m)` that takes two integers `n` and `m` as input and calculates the average of the two integers. Since the average is computed halfway between the two numbers, the average is rounded to the nearest integer. The result is then converted to a binary string, and if the conversion results in a non-alphabetic string, it's prepended with '0b' to ensure a valid binary string. The function returns '-1' if `n` is greater than `m`, and the example usage and corresponding output demonstrate how the function behaves for various input scenarios.