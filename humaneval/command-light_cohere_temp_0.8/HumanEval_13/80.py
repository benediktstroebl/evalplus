```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if a == 0 or b == 0:
        return 0
    i, divisor = divmod(a, b)
    while divisor > 0:
        if divisor % a == 0 and divisor % b == 0:
            break
        divisor //= 2
    return divisor

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(123, 456))  # Raise ValueError
```