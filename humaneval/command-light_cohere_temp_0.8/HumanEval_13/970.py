```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    while b != 0:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(1, 5))   # Raises ValueError
print(greatest_common_divisor(7, -1)))  # Raises ValueError
print(greatest_common_divisor(0, 5))    # Raises ValueError
```