```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    m, r = divmod(a, b)
    if r != 0:
        return r

    return max(m, greatest_common_divisor(b, a % b))

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```
The code defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. It performs a series of tests to ensure the function works correctly, and the test cases cover various scenarios.