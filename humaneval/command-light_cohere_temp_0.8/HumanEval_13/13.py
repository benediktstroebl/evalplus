```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    max_ = max(a, b)
    min_ = min(a, b)
    for i in range(1, max_divis_available = False
            while a % i == 0 and b % i == 0:
                a //= i
                b //= i
                max_divis_available = True
                if max_divis_available:
                    break
            if max_divis_available:
                break
        return max()
    
# Tests
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(2, 5))  # Should return 0, however, Python 2 behaves this way)
print(greatest_common_divisor(9, 12))  # Output: 3
```
The script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. It uses two passes: one to handle edge cases (when either input is 0) and the other loop to find the greatest common divisor for the given inputs.  The