```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This algorithm utilizes Euclidean algorithm to find the greatest common divisor. The algorithm uses the principle that the remainder of the division always provides the smaller number required for the subsequent step until it becomes 1. 

Here is an example:
```python
>>> greatest_common_divisor(40, 56)
8
```