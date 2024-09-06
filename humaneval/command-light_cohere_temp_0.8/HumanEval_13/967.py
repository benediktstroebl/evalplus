```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be set")
    return max((c for c in range(1, max(a, b)) if c is_divisible(a, b)))

def is_divisible(a: int, b: int) -> bool:
    return (a == 0 or b == 0) or a % b == 0

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(2, 3))  # Should raise ValueError
print(greatest_common_divisor(6, 2))  # Should raise ValueError
```
The function `greatest_common_divisor` calculates and returns the greatest common divisor of two integers `a` and `b`. The function also has two helper functions:
1. `is_divisible(a, b)` checks if `a` is divisible by `b`.
2. This function returns `True` if `a` is 0 or `b` is 0, or `a % b == 0` otherwise. 
Note that the function does not check if `a` or `b` are actually divisible by each other. 
The main function checks if both `a` and `b` are set (not `None`), and raises a `ValueError` if they are not. If they are, it finds the greatest common divisor using a list comprehension and returns the result.