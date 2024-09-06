```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This algorithm optimizes processing using the Euclidean algorithm and utilizes a recursive approach to find the GCD. It exploits the property that the GCD of any integer `x` and `0` is `x`. 
It offers a concise solution to the problem. To use this function, ensure you have imported the math library, as shown below:
```python
import math
``` 
This allows you to call the function and utilize its functionality.