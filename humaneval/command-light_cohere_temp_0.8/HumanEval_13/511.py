```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero.")
    gcd = 1
    while b != 0:
        gcd = a % b
    return gcd
# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(6, 20))  # Should raise ValueError
```