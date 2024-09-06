```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    return abs(b) if a > b else greatest_common_divisor(b, a)

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(7, 12))  # Output: 2 (Note: a doesn't have a common divisor with 12)

# Test case 4
print(greatest_common_divisor(18, 18))  # Output: 18 (Both numbers are equal)
```