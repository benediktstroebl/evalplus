```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    while a != 0 and b != 0:
        a, b = divmod(a, b)

    return max([a, b])

# Test the function with various inputs
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(3, 15))  # Output: 5
print(greatest_common_divisor(9, 27))  # Output: 3
print(greatest_common_divisor(81, 99))  # Output: 17
```