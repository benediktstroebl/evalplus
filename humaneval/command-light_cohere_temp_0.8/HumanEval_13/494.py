```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    while b != 0:
        if a % b == 0:
            a, b = b, a
        else:
            break
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(12, 56)))  # Output: 4
print(greatest_common_divisor(0, 5))    # Expected ValueError: Both numbers must be positive
```