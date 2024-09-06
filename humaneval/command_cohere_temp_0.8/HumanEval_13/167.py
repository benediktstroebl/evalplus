```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```

This algorithm exploits the property of Euclidean Algorithm wherein the modulo operation accelerates the reduction of division steps needed to compute the GCD. It is an iterative algorithm that repeats the above step until b becomes zero. Since the GCD of any number and zero is that number itself, the algorithm stops when b becomes zero, and returns a if b was zero since the GCD of a and 0 is always a.