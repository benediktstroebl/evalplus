```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a recursive function `greatest_common_divisor` that returns the greatest common divisor of two integers a and b. The base case of the recursion is when b is 0; in this case, the function returns a. Otherwise, the function calls itself recursively with the arguments b and a % b, which represents the remainder of the division of a by b. 

The function uses the Euclidean algorithm for computing the GCD, which is a widely used linear time method for finding the greatest common divisor of two integers.