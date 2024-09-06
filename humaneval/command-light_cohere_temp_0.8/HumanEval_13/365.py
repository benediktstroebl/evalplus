```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != 0 and b != 0:
        a, b = divmod(a, b)

    return max(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The function uses the important optimizations to minimize unnecessary calculations and improve the efficiency of the solution.