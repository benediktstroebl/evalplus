```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This algorithm utilizes the Euclidean algorithm to find the greatest common divisor. It recursively divides the larger number by the smaller number, returning the remainder to the smaller number. This process continues until the remainder becomes zero, at which point the smallest number will be the greatest common divisor. 

Here is a quick breakdown of the code:
1. If `a` is 0, we return `b` since `b` must be the GCD if `a` is divisible by `b` and the remainder is `b`.
2. If the remainder of the division `b%a` is 0, it means that `a` is the GCD.
3. Otherwise, we keep dividing `b` by `a` and return the remainder until `b` becomes 0. The GCD will be the last value of `a` returned.

This algorithm is known for its efficiency due to the optimized use of `a` and `b` in the division and remainder calculations. The Euclidean algorithm's genius lies in the realization that the greatest common divisor behaves like the remainder of a continually divided pair of numbers.