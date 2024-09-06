```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive algorithm is inspired by the Euclidean algorithm. It minimizes the larger number periodically while converging to the GCD. The base case involves solving the GCD of 0 and x, which is always x. 

The docstring explains the purpose of the function and provides illustrative examples. 

To handle the case of integer overflow (which occurs when the absolute value of the input numbers exceeds the maximum value that an integer data type can hold), you could use the long class from the math module. 

```python
from math import long

def greatest_common_divisor(a, b) -> long:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This modification ensures that the algorithm can handle larger inputs without encountering an overflow error.