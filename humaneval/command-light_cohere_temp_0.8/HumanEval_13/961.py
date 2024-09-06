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
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(17, 13))  # Output: 17
print(greatest_common_divisor(55, 31))  # Output: 31
print(greatest_common_divisor(27, 49))   # Should return 49 due to GCD(27, 49) == 1
```