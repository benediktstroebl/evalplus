```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The `greatest_common_divisor` function employs recursion to find the greatest common divisor (GCD) of two integers `a` and `b`. It leverages the property that the GCD of two numbers `x` and `y` is the same as the GCD of `y` and `x % y`. If `b` is 0, it means that `a` is the GCD, hence the function returns `a`. Otherwise, the function recursively calls itself with the arguments `b` and `a % b`, which are guaranteed to produce the same GCD as the original numbers `a` and `b`.