```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b % a, a)
```
This script defines a recursive function 'greatest_common_divisor' that calculates the GCD of two integers a and b. It employs the Euclidean algorithm to find the GCD by repeatedly subtracting the smaller number from the larger one until the remainder is zero. The result is the GCD of the initial two numbers. 

The function handles the edge case where one or both inputs are 0 to ensure it doesn't result in an infinite loop.

The function is encapsulated in a testable manner. When invoked with distinct input values, it accurately outputs the anticipated greatest common divisors (GCDs).

If needed, docstrings and more thorough testing can increase the function's readability and usefulness even more.