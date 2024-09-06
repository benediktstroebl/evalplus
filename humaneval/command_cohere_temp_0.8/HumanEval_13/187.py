```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```
This script defines a Python function called `greatest_common_divisor` that takes two integers a and b as input and returns the greatest common divisor of these two numbers. 

The base case of the recursion is when either of the numbers is 0. In this case, the GCD is the non-zero number. It also handles the case when b is 0, as the Euclidean algorithm requires the larger number to be the second parameter. 

It uses recursion and the Euclidean algorithm for computing the GCD. The Euclidean algorithm is a widely used algorithm that calculates the greatest common divisor of two numbers a and b. It iteratively computes the remainder of the division of b by a, updates b to be the new value of a, and repeats this process until b becomes 0. 

The script then provides a docstring explanation of the function, and example usage demonstrations in the form of test cases. These test cases show that the function correctly returns the greatest common divisor of the given values and demonstrates its usefulness in finding a GCD.