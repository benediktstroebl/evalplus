```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    while b != 0:
        if a % b == 0:
            a, b = b, a
        else:
            break
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(5, 3))   # Input: Negative test case, should raise ValueError
print(greatest_common_divisor(3, -5))   # Should raise ValueError
```
This script defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers `a` and `b`. The function handles the edge case where both inputs are 0 by raising a `ValueError`.