```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    gcd = 0
    while b > 0:
        a, b = b, a % b
    gcd = a
    return gcd

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(36, 48)))  # Output: 12
print(greatest_common_divisor(36, 27)))  # Should return 36
```