```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This script defines a recursive function `greatest_common_divisor` that returns the greatest common divisor of two integers `a` and `b`. It exploits the fact that the `GCD` of a number `x` and 0 is `x`. 

Here is an example usage of the function:
```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
>>> greatest_common_divisor(0, 31)
31
```
This example demonstrates the function's behavior for different cases.