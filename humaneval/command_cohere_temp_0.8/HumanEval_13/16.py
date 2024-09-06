```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The `greatest_common_divisor` function employs recursion to find the greatest common divisor (GCD) of two integers `a` and `b`. It leverages the property that the GCD of two numbers `x` and `y` is the same as the GCD of `y` and `x % y`, alleviating the need to compute the GCD of `b` and `a % b` directly. 

Here's an example usage of the function:
```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
```
This script ensures that the GCD is returned for any two integers `a` and `b`, handling the case where `b` is 0 intentionally to comply with the specification of the GCD algorithm.