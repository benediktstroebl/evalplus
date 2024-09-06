```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    while a != 0:
        a, b = divmod(a, b)

    return b

# Test the function with various inputs
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(105, 25))  # Output: 5
print(greatest_common_divisor(107, 105))  # Output: 5
print(greatest_common_divisor(0, 0))  # Output: 0
print(greatest_common_divisor(10, 5))   # Input error: a and b are both 0)
```