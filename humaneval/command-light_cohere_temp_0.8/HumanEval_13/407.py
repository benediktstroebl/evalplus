```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero")
    while b != 0:
        if a % b == 0:
            a, b = b, a
        else:
            b = b // gcd(a, b)
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(3, 15))   # Should raise ValueError
```