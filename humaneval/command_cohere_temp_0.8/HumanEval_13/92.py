```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This algorithm utilizes Euclidean algorithm to find the greatest common divisor. The algorithm works by calculating the remainder of division of a by b, and then considering the smaller number as the new 'b' and repeating the process until b becomes 0.  The number a will eventually become 0 as well, and the greatest common divisor is the absolute value of 'a' at the moment when both a and b become 0.