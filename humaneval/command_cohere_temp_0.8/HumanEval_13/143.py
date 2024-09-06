```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The logic is based on the calculation of the greatest common divisor (GCD) of two numbers `a` and `b`. The `GCD` of two integers is the largest positive integer that divides both numbers evenly. The `GCD` of `0` and any number is always `0`, so the case `b == 0` is handled separately. In the general case, the `GCD` of `a` and `b` is calculated using the Euclidean algorithm successively applying the formula `GCD(b, a % b) = GCD(b, b % a)`. This algorithm gradually reduces the larger of the two numbers to a zero divisor, producing the `GCD` of the two initial numbers. 

The docstring explains the purpose of the function and provides example outputs. These examples validate the correct behavior of the function:
```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
```