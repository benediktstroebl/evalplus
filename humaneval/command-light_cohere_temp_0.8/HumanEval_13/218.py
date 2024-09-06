```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    while a % b == 0:
        a, b = b, a
    
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```
The script defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers `a` and `b`. The function runs a loop, continually dividing the larger number by the smaller one, until the smaller number is no longer divisible by the larger. The final value of `a` is returned.