```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This algorithm optimizes a recursive approach to computing the GCD using the Euclidean algorithm. It avoids redundant calculations by adjusting the recurrence relation. This optimization saves computational resources, making the algorithm more efficient and quicker, improving its time complexity to O(log(min(a,b))).