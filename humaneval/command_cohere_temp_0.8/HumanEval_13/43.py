```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Recursive approach for computing the GCD of two numbers is efficient and uses the Euclidean Algorithm for computing the GCD. The case b == 0 is handled separately since the Euclidean algorithm doesn't work without division by zero errors when b is 0. In this case, it directly returns a since the GCD of any number and 0 is the number itself. 

The recursive call is made with the arguments in the reverse order and a % b to ensure that the smaller number is used as the dividend in each recursive call. This approach drastically reduces the number of divisions needed to find the GCD, making it efficient for computing the GCD of 2 numbers. 

The function heading indicates that the result is int, meaning that the result will be cast to an integer type, and any decimal values resulting from calculations will be truncated.  This is a useful indication to include when there is a possibility that the result could be a decimal value.  In this case, it is not necessary since the Euclidean Algorithm is guaranteed to produce an integer value.  It is good to keep this in mind for future consideration when developing functions that may produce decimal results.