```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    if a == 0:
        return b
    if b == 0:
        return a

    while a != 0:
        a, b = b % a, b

    return b

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(6, 30)))  # Output: 1
print(greatest_common_divisor(0, 7))  # Output: 7
print(greatest_common_divisor(10, 55))  # Should return 10 not divisible by 0)
```