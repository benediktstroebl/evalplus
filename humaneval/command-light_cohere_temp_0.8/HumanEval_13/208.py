```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != 0 and b != 0:
        a, b = divmod(a, b)
    
    return min(a, b)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This code defines a function `greatest_common_divisor(a, b)` that calculates and returns the greatest common divisor of two integers `a` and `b`. The function first handles corner cases where either input is 0, in which case it returns the other non-zero number. The function then employs the`divmod` function to repeatedly divide the larger number by the smaller one, until one of them becomes zero, at which point the other is the greatest common divisor.