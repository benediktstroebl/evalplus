```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The algorithm works by recursively dividing the larger number by the smaller one and taking the remainder. This loop continues until the smaller number becomes zero, at which point the larger number is the required GCD. In the case where b is zero, a is the GCD, and the function returns a. You can test the function by calling it with different pairs of integers. 

For example:
```python
>>> greatest_common_divisor(60, 48)
8
```