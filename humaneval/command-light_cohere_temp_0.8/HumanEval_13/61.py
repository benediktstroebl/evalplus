```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a

    while a % b == 0:
        a //= b
    else:
        return a  # return the larger value if b doesn't divide a evenly

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(12, 5))  # Output: 5
print(greatest_common_divisor(10, 15)))  # Should raise an error: 10 doesn't have a GCD with other numbers
```