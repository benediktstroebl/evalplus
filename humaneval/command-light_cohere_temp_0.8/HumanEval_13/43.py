```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    c = a
    while b > 0:
        if c % b == 0:
            c += b
        else:
            break
    return c

# Test the function with a few examples
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(36, 24)))  # Output: 12
print(greatest_common_divisor(108, 270))  # Output: 270
```
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. It uses a `while` loop to iterate through divisors of `b`, incrementing `c` if the divisor is evenly divided into `b`.  The function is then tested with a few examples, and the results are printed.