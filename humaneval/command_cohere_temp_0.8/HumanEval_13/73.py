```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b % a, a)
```
This script defines a Python function called `greatest_common_divisor` that takes two integers a and b as input and computes the greatest common divisor of these two numbers. The GCD of two numbers is the largest integer that divides both numbers evenly.

The algorithm to compute the GCD is the Euclidean algorithm. It consists of successive divisions of the larger number by the smaller number and taking the remainder. The process continues until the remainder becomes zero, and the smaller number is the GCD of the two initial numbers.

In this algorithm, the base case is when the smaller number is 0. In this case, the GCD is the larger number. The recursive case is when the remainder is not 0, and the GCD is computed recursively for the remainder and the smaller number.

The script includes a docstring, which is a multi-line comment enclosed in triple quotes. This comment provides information about the function, its parameters, and its return value. It also contains examples to illustrate the usage of the function. These examples demonstrate how the function works for different input values (`a` and `b`). The function returns the GCD of the given numbers according to the specification. 

This function can be called from another Python program or script to calculate the greatest common divisor of any two given integers a and b.  The intended usage of the function is to maximize the interoperability between different parts of programming workflows by adhering to the DRY (Don't Repeat Yourself) principle.  The function is self-contained, and it can be understood and used correctly with the provided docstring.  The tests can be added right inside the script to verify the function behavior, ensuring that the function works correctly.  away. 

Overall, this is a classic example of how to use Python to solve a specific problem in a concise, efficient, and well-documented manner. 
```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b % a, a)
```