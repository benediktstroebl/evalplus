```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This version of the function uses the Euclidean algorithm for computing the GCD. 
It is expressed with recursion and utilizes the fundamental property that the GCD of a number and its dividend is the same as the GCD of the dividend and the remainder. 

Here are some example inputs and outputs to test the function:
```
>>> print(greatest_common_divisor(48, 36))
12
>>> print(greatest_common_divisor(40, 75))
5
>>> print(greatest_common_divisor(0, 100))
100
>>> print(greatest_common_divisor(100, 0))
100
```