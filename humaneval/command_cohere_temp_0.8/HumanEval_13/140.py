```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b % a, a)
```

The algorithm for determining the greatest common divisor (GCD) is based on Euclidean algorithm Synthetic Division. It is called synthetic because it mimics the workings of the natural division process. The method is recursive, where the quotient is calculated internally in order to avoid multiple iterations.

This algorithm has a time complexity of O(log(min(a,b))). 

The function includes docstrings and annotations that explain its purpose, input, and output for better readability and maintainability. 

To ensure correctness, this function should pass tests including edge cases like `greatest_common_divisor(0, 0)`, `greatest_common_divisor(1, 1)`, and `greatest_common_divisor(36, 10)`.