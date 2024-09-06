```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This algorithm exploits the property of Euclidean Algorithm wherein the absolute values of the operands tend to converge towards the final result. Thus in the worst case, the algorithm would require at most *log*(*min(*a*,*b*)*) iterations to converge.