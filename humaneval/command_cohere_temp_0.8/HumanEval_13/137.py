```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This version of the function uses the Euclidean algorithm for computing the GCD. 
It is expressed as a recursive function, where the base case occurs when b is 0, 
returning a in such a case. Otherwise, the function recursively calls itself with 
the arguments flipped, with the modulo operation (a % b) ensuring that the 
recursion eventually terminates. 

This approach is efficient due to the modulo operation preventing infinite 
cycles in case of a large difference between the input integers.