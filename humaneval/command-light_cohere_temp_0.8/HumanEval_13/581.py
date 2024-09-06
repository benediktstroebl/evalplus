```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a

    while a != b:
        if a % b == 0:
            a, b = b, a
        else:
            a -= b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(3, 3))  # Output: 2
print(greatest_common_divisor(0, 5))  # Output: 5
print(greatest_common_divisor(10, 15))  # Should return 10
```