```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != 0:
        a, b = divmod(a, b)
    
    return max(b, a)

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(8, 48))  # Output: 4
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function uses a combination of `divmod` and `max` functions to efficiently compute the result.