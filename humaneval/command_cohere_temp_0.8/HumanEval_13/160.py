```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This algorithm utilizes Euclid's algorithm to find the greatest common divisor between two integers `a` and `b`. It is computationally efficient and is optimized for readability and ease of use.