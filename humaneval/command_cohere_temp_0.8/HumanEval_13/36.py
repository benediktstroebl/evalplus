```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The logic of this approach is to use recursion by transforming the equation `x * b = a` into `x = a // b` which gives the GCD of `a` and `b`. In the case where `b` is 0, it is better to return `a` as `a` will be the GCD of `a` and `0`. 

This approach isn't the most efficient one as it has a time complexity of O(n) and uses the Euclidean Algorithm. There are faster approaches with faster time complexities.