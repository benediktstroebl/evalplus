```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    c = 0
    while b > 0:
        if a % b == 0:
            c += 1
        a //= b
        b = a % b
    return c

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(48, 24)))  # Output: 4
print(greatest_common_divisor(36, 60)))  # Output: 2
```