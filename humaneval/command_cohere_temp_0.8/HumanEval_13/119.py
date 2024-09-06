```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The `greatest_common_divisor` function employs the Euclidean algorithm to find the greatest common divisor (GCD) of two integers `a` and `b`. It repeats the process recursively, alternating between dividing `a` by `b` and dividing `b` by `a` modulo `b`, until `b` is zero. At this point, the GCD is `a`. 

The algorithm leverages the property that the GCD of two numbers `x` and `y` is the same as the GCD of `y` and `x % y` if `y` is not zero.