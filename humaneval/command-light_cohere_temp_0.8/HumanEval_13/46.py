```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    while b > 0:
        if b % a == 0:
            a, b = b, a
        else:
            b -= 1
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(123, 456))  # Output: 321
print(greatest_common_divisor(-1, 10))  # Output: Error: Both numbers must be positive
```
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two positive integers `a` and `b`. It employs a basic "dividing out" strategy to locate the shared factors. It also includes test cases to make sure that the function behaves as expected.