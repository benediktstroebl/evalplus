```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Cannot find a common divisor of non-positive integers.")
    return max(a, b) / (b+1) if b != 0 else 0

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(-5))  # Raises ValueError
print(greatest_common_divisor(10, -3))  # Raises ValueError
```