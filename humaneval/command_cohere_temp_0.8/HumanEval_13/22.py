```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The `greatest_common_divisor` function employs the Euclidean algorithm for finding the greatest common divisor (GCD) of two integers `a` and `b`. If `b` is 0, it returns `a` since `a` is the GCD of any number and 0. Otherwise, it recursively calls itself with arguments `b` and `a % b`, which represents the remainder of the division of `a` by `b`. This process continues until `b` becomes 0, at which point the GCD is found, and the intermediate remainders are used to compute it. 
The base case ensures that the algorithm terminates correctly and handles potential infinite recursion caused by `b` being 0.