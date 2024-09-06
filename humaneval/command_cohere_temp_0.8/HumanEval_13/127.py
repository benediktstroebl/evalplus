```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b % a, a)
```
This recursive algorithm is inspired by the Euclidean algorithm. It works by the following steps:
1. If either number is 0, the GCD is the other number.
2. Otherwise, the GCD is the GCD of the second number divided by the first number (b%a) and the first number (a).

The above steps repeat until the second number (b) becomes 0. At that point, the GCD is the first number (a).

The algorithm benefits from the property that the GCD of two numbers `a` and `b` is the same as the GCD of `b%a` and `a`. 

This algorithm is efficient for computing the GCD of two integers a and b. It is a recursive algorithm that uses the Euclidean algorithm as its fundamental principle. 

It is worth noting that the above algorithm is not the most efficient approach for calculating the GCD, as it requires multiple recursive calls. Given the iterative nature of the problem, it is easier to optimize it using memoization to avoid redundant recursive calls. However, the above approach is straightforward and simple to implement. 

It's important to ensure that you are working with integers throughout the algorithm, as floating-point numbers can introduce inaccuracies in the computations. You may consider using the `int()` function to cast the inputs and outputs to integers, ensuring precise results. 

Please note that the script assumes that the inputs are valid integers, and no explicit checking is done for invalid inputs. Depending on the specific use case, you might want to add additional error handling or input validation to handle edge cases and improve the robustness of the solution.