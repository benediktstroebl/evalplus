```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This code defines a Python function called `greatest_common_divisor` that takes two integers a and b as input. It is a recursive algorithm that utilizes the Euclidean algorithm to find the greatest common divisor (GCD) of the two numbers. 

Here's how it works:
1. In the base case, if b is 0, the function returns a since it is an infinite divisor of a.
2. If b is not 0, the function calls itself recursively, passing the arguments b%a (the remainder of b divided by a) and a. 

This recursive approach continues until b becomes 0, at which point the recursion unwinds and the GCD of the original inputs a and b is found. The GCD is returned as the result.

Please note that this approach leverages Python's built-in modulo operator (%) and recursion to efficiently compute the GCD, making it an optimized solution for finding the greatest common divisor.