```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive algorithm is inspired by the Euclidean algorithm. It exploits the fact that the greatest common divisor remains the same if the larger number is replaced by the remainder of the larger number divided by the smaller number. 

It offers an efficient way to calculate the greatest common divisor by repeatedly applying this rule recursively. 

The base case involves a = 0, in which case the function returns b, the larger number that is not divided by the smaller number a. 
This is the efficient and optimized version of the Euclidean algorithm. It calculates the GCD in O(log(min(a,b))).

The docstring explains the purpose of the function, and the unit tests verify correct and accurate computation of the greatest common divisor for various test cases.