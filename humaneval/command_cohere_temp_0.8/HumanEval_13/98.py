```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This code defines a Python function called `greatest_common_divisor` that takes two integers a and b as input. It is a recursive algorithm that utilizes the Euclidean algorithm to find the greatest common divisor (GCD) of the two numbers.

The Euclidean algorithm iteratively computes the GCD by considering the remainder of successive divisions. The algorithm recursively calls itself with the arguments b%a (the remainder of b divided by a) and a. It alternates between these two arguments until a reaches zero, at which point the current value of b is the GCD of the original a and b.

The base case of the recursion is when a becomes zero. In this case, the function returns b as the GCD, since b is necessarily a factor of a and b, and greatest among all common divisors at this point.

The `greatest_common_divisor` function's usage example demonstrates how it can be called to compute the GCD of 3 and 5, resulting in a return value of 1. Similarly, it calculates the GCD of 25 and 15 correctly, yielding 5. These examples showcase the function's ability to determine the GCD effectively.