```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a recursive function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two given integers `a` and `b`. It utilizes the Euclidean algorithm to find the GCD. If `b` is zero, it returns `a` since `a` is the GCD of any number and zero. Otherwise, it recursively calls itself with the arguments `b` and `a % b`, which represents the remainder of the division of `a` by `b`. This process continues until `b` becomes zero, at which point the GCD is found, and it returns this value.