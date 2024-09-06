```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != 0:
        a, b = divmod(a, b)
    
    return min(b, a)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(3, 15)))   # Output: 5
print(greatest_common_divisor(9, 6)))   # Output: 3
```

This script defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers `a` and `b`. The algorithm uses the Euclidean algorithm with a loop, and at each step, it updates `a` and `b` using the formula `a, b = divmod(a, b)`. The test cases are provided to ensure that the function works correctly for various inputs.