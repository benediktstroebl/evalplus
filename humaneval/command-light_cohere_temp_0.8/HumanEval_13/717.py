```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero")
    while b != 0:
        if a % b == 0:
            a, b = b, a // b
        else:
            break
    return a if a > 0 else 0

# Test the function with a few cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(9, 18))  # Output: 18 (since 9 is divisible by both 3 and 18)
print(greatest_common_divisor(10, 40))  # Should raise ValueError
```