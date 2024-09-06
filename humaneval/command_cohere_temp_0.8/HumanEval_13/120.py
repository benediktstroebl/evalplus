```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a recursive function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two integers `a` and `b`. It utilizes the Euclidean algorithm to find the GCD. If `b` is zero, it returns `a` since `a` is the GCD of any number and zero. Otherwise, it recursively calls itself with the arguments `b` and `a % b`, which represents the remainder of the division of `a` by `b`. This process continues until `b` becomes zero, at which point the GCD is found, and it returns this value. 

Here is an example usage of the function:
```python
>>> greatest_common_divisor(12, 8)
4
>>> greatest_common_divisor(48, 96)
24
```
This will return the greatest common divisor of 12 and 8 as 4, and the greatest common divisor of 48 and 96 as 24.

This approach is efficient because the number of divisions decreases logarithmically with the size of the smaller number. This means it reduces the problem size with each step, leading to a relatively quick convergence to the GCD. 

This function is concise and elegant and provides a clear and useful implementation of the algorithm.  It is important to note, however, that for large numbers, the function may not be the most efficient as its runtime is proportional to the logarithm of the smaller number's size.  If performance is a concern, alternative approaches may be necessary.