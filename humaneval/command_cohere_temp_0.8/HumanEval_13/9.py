```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

This script defines a recursive function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns the greatest common divisor of the two integers. The base case of the recursion is if `a` or `b` is zero, in which case the other number is returned. If neither number is zero, the function recursively returns the greatest common divisor of `b%a` and `a`. 

This would yield a markdown code block:
```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```