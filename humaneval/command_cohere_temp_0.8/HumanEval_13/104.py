```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a recursive function `greatest_common_divisor` that finds the greatest common divisor of two integers `a` and `b`. It makes use of the Euclidean algorithm for computing the GCD. If `b` is zero, it returns `a` since `a` is the GCD of any number and zero. Otherwise, it recursively calls itself with the arguments `b` and `a % b`, which represents the remainder of the division of `a` by `b`. 

The base case ensures that if one of the input values is zero, the function returns the other input since the GCD of a number and zero is that number. This approach ensures that the function progressively narrows down the GCD of the two numbers until it reaches the correct value.