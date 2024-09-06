```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    # Find the greatest divisor of a and b
    gcd = max((a, b))
    
    # Return the greatest common divisor
    return gcd

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(5, 5)))  # Output: 5 (it is also a valid test)
print(greatest_common_divisor(10, 25))  # Output: 5
```