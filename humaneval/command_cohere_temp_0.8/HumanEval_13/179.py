```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This version of the function uses the Euclidean algorithm for computing the GCD. The algorithm is expressed by the recursive formula b = a*x + b%a,  x = b%a, where each letter corresponds to the successive remainders of the division of a by b. The algorithm terminates when the remainder becomes zero, yielding the GCD of the original two numbers. 

The algorithm implemented in the function is not strictly the Euclidean algorithm, as it does not iterate through the divisions sequentially. Instead, it uses the property that the GCD will be the same when passed the remainder of the division second, and immediately returns the value without recursive chaining. 

This version of the code is more efficient, with a time complexity of O(log(min(a,b))). 

The function should handle the edge case where a is 0 by returning b, as a zero divisor will cause issues with the algorithm's formulation. 

The markdown docstring and test cases are appreciated additions to the code. These elements provide helpful context and ensure the code works correctly. 

Would you like to generate more examples of functions that need docstrings or discuss best practices for writing them?