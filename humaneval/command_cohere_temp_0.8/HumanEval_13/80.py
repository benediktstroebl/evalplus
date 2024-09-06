```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The GCD algorithm works by recursive elimination of multiples of one integer from the other. Given two integers a and b, the greatest common divisor is the largest integer that divides both a and b without remainder. It can be understood as the lowest common multiple of a and b, except that divisors are always greater than zero. 

This algorithm is commonly used in conjunction with the Euclidean Algorithm, which relies on the principle that the GCD of two numbers `x` and `y` is the same as the GCD of `y` and `x % y` (`x` modulo `y`). 

It is worth noting that the algorithm terminates since the function calls itself with decreasing arguments until b becomes 0. At each step, the remainder (`a % b`) becomes the new b parameter, and the process continues until the remainder becomes 0. 

This is a common optimization of the basic Euclidean Algorithm, which iteratively calculates the remainder after division, resulting in a slower process for larger integers.