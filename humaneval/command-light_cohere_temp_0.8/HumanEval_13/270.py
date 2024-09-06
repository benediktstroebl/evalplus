```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(6, 10))  # Output: 6
print(greatest_common_divisor(12, 27)))  # Output: 3
```
This Python function, `greatest_common_divisor`, computes the greatest common divisor of two integers `a` and `b`. It employs a basic loop, checking each divisor of `b` in turn with the remainder of `a` divided by `b`. It returns `0` if either number is zero, or the other is zero. If both are non-zero, the function recursively calls itself with the GCD of the other number and the divisor.