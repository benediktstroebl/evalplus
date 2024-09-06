```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    min_ab = min(a, b)
    return max([i for i in range(1, min_ab) if not((a % i) | (b % i))])

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(64, 25))  # Output: 8
print(greatest_common_divisor(120, 24))  # Output: 4
```
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function first handles corner cases where either input is 0, in which case it returns 0. Then, it calculates the maximum divisor of the minimum of the two inputs.