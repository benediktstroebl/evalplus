```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return 0
    if b == 0:
        return 0

    # Find the greatest common divisor
    temp = a
    while b != 0:
        if b % temp == 0:
            temp = b
        b = b // temp

    return temp

# Test the function with simple inputs
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(4, 6))  # Output: 2
print(greatest_common_divisor(10, 55))  # Should raise an error: 10 and 55 don't have a greatest common divisor)
```