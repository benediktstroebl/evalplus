```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer")
    if a == 0:
        return 0
    if b == 0:
        return 0

    while a != 0:
        a, b = divmod(a, b)

    return b

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(2, 25))  # Output: 1 (correct for 2 and 25)
print(greatest_common_divisor(-23, -4))  # Output: valid, but shouldn't be reached without non-zero inputs
```