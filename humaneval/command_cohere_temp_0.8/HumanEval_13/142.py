```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The function is based on the Euclidean algorithm that uses the property that the gcd of two numbers `a` and `b` is the same as the gcd of `b` and `a % b`. The base case is when `b` is 0, where the gcd is `a`. 

This algorithm is very efficient and has a time complexity of O(log(min(a,b))).