```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This version of the code uses Euclidean algorithm with recursive approach. 

The function returns the greatest common divisor of two integers a and b. It also handles the case when a is 0, hence the recursive call is actually b%a in this case, which simulates the division with remainder (aka modulo) and avoids potential infinite loop when a is 0.