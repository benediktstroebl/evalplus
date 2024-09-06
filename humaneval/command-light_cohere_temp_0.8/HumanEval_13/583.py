```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("One or both arguments must be a non-zero integer.")
    return max((i) for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(123, 456))  # Output: error: ValueError: One or both arguments must be a non-zero integer.
```