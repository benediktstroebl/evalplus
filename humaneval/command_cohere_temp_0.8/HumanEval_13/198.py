```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive approach is quite common and uses the Euclidean algorithm to efficiently compute the GCD. The base case of the recursion is when either number is 0, at which point the other number is divisible by it and therefore the GCD. 

Unfortunately, this approach suffers from the deficiency of infinite recursion for cases where a or b is 0, as no actual division is performed, and the function simply keeps substituting the larger number with the remainder of the larger number divided by the smaller number.