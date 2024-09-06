```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    elif b == 1:
        return a
    elif a == 1:
        return b
    else:
        return greatest_common_divisor(b, a % b)
```
This code defines a recursive function greatest_common_divisor that calculates the greatest common divisor of two integers a and b. Recursively, it first checks if both a and b are equal to 0 or 1. If b is 1, it returns a, if a is 1, it returns b. If neither a values are equal to 1, it recursively calls itself with the other parameter, continue this process until a common divisor is found.