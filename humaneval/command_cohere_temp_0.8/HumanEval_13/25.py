```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This version of the function uses the Euclidean algorithm for computing the GCD. 
It is called with two integers `a` and `b`. It returns the GCD of these numbers. 
If `a` is 0, the function returns `b` without performing unnecessary computations. 
The function is designed to be called recursively, with the smaller integer argument first, followed by the larger integer argument. 
This approach helps to reduce the number of iterations required to find the GCD. 
The base case of the recursion is when either of the integers is 0, where it returns the other integer. 
This is because the GCD of 0 and any other number is the other number itself. GCD()