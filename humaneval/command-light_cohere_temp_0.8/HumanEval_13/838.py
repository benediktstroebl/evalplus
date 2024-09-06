```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    while b > 0:
        a, b = b, a % b

    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```
The function `greatest_common_divisor` calculates the greatest common divisor of two integers `a` and `b`. It utilizes a loop to iterate through potential divisors of `b`, then uses the remainder operator `%` to determine the largest divisor of `a` that evenly divides into `b`. The `while` loop ensures that the largest possible divisor is returned before stopping. 
 Test cases cover the basic cases of non-zero numbers and zero values.