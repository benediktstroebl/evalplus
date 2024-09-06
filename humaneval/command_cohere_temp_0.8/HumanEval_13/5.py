```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This algorithm utilizes Euclidean algorithm to find the greatest common divisor between two integers `a` and `b`. It is efficient, with a time complexity of O(log(min(a, b))) iterations. The algorithm's approach is to continually find the remainder of `a` divided by `b`, and use the smaller number as the dividend for the next step. This continues until the dividend is 0, at which point the divisor will be the GCD. The algorithm then iteratively returns the divisor as the base case, and returns the largest number which is divisible by both `a` and `b`.