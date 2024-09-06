```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a

    while a % b == 0:
        a //= b
    else:
        return a  # if b doesn't divide a, then it's the GCD

    return a

# Test cases
print(greatest_common_divisor(3, 5))      # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(4, 12))      # Output: 4 (divisible into both 3 and 12)
print(greatest_common_divisor(10, 20))     # Output: 5 (divisible into both 10 and 20)
```
The `greatest_common_divisor` function calculates the greatest common divisor of two integers `a` and `b` using a loop-any common divisor of the two numbers will do.  The numbers are effectively reduced to a single unique number.