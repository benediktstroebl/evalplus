```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```

This recursive approach to finding the greatest common divisor is very efficient and elegant, but it's good to be mindful of potential edge cases (like when arguments are close to zero) that could lead to undesired performance behavior.