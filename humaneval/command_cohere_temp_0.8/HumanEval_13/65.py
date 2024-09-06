```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This algorithm works by the Euclidean algorithm idea of taking the remainder of division of the larger number by the smaller number, considering the smaller number as the new larger number, and repeating this process until the remainder becomes zero. At this point, the smaller number is the GCD of the two given numbers. This algorithm is very efficient, and the computation of GCD needs not calculate the division operation, making it faster.