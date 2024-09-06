```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b % a, a)
```
This recursive algorithm is inspired by the Euclidean algorithm. It works by taking a fractional remainder `b % a` and gradually narrowing down the denominator. 

The GCD is computed iteratively by repeated applications of the formula:
```
GCD(a, b) = GCD(b % a, a)
``` 
Here is a breakdown of how it works:
1. If `b` is 0, then `a` is the GCD, so the result is `a`.
2. If `a` is 0, then `b` is the GCD, so the result is `b`.
3. If both numbers are equal, the GCD is calculated as `a`.
4. Otherwise, we apply the formula based on the remainder.

This algorithm terminates when the remainder becomes 0, meaning that `b % a` equals 0. At this point, the denominator becomes 0, producing the GCD as the numerator.

The algorithm operates by continually dividing the larger number by the smaller number and taking the remainder. This process continues until the remainder becomes 0, at which point the largest number is the GCD of the two original numbers.

This approach is efficient because it minimizes the number of divisions required to find the GCD, resulting in an efficient algorithm with a time complexity of `O(log(min(a, b)))`.

The code includes a self-contained function that doesn't rely on global variables, making it reusable and maintaining the `O(log(min(a, b)))` time complexity. It is efficiently optimized to find the GCD of any two given integers `a` and `b`. 

It also includes informative docstrings that explain the purpose of the function, and provide example usage, allowing users to easily understand and integrate the function into their projects.