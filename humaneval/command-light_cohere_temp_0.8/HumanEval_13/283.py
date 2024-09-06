```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")

    if a == 0:
        return b
    elif b == 0:
        return a

    while a != 1:
        a //= b
    while b != 1:
        b //= a

    return min(a, b)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(4, 12))  # Should raise ValueError
```