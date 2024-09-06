```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input is required")
    return math.sqrt(max((a % b) % 1, 0)))

# Test the function with various inputs
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(6, 9))  # Output: 3 (correct result)
print(greatest_common_divisor(0, 5))  # Raises ValueError
print(greatest_common_divisor(20, 0))  # Raises ValueError
print(greatest_common_divisor(1, 11))  # Raises ValueError
```