```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(13, 49))  # Output: 13 (since 13/49 is 13)
print(greatest_common_divisor(19, 121)))  # Should return 19
```