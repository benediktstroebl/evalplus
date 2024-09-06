```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This algorithm works by the Euclidean algorithm concept, which states that the absolute values of the GCD of two numbers `x` and `y` is the same as the GCD of `y` and `x % y`. The algorithm terminates when `y` becomes 0, at which point the remaining value of `x` is the GCD of the two initial numbers. 
The algorithm implemented this way is recursive, meaning the function calls itself to solve a smaller instance of the same problem.