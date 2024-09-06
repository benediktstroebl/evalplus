```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Two numbers must be provided.")
    while a % b == 0:
        a //= a // b
        b = b - (a // b)
    return min([a, b])

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(3, 10))  # Raises ValueError
print(greatest_common_divisor(6, 2))  # Raises ValueError
```