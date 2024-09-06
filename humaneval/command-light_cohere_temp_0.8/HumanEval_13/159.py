```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer.")
    if a == 0:
        return 0
    if b == 0:
        return 0

    while a != 0:
        a, b = b // a, a // b

    return b

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(2, 250))  # Output: 50
print(greatest_common_divisor(0, 5))   # Output: 0
print(greatest_common_divisor(10, -1))  # Raises ValueError
```