```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a function `greatest_common_divisor` that finds the greatest common divisor of two integers `a` and `b`. It uses Euclidean algorithm for computing the GCD. If `b` is zero, it returns `a`. Otherwise, it recursively calls itself with arguments `b` and `a % b`, which represents the remainder of the division of `a` by `b`. This process continues until `b` becomes zero, at which point the GCD is found and returned.