```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Cannot calculate GCD of zero numbers")
    return math.gcd(a, b)
```
This code defines a function `greatest_common_divisor` that computes the greatest common divisor of two numbers `a` and `b`. The function uses the built-in `math.gcd()` function to calculate the gcd of two numbers. The function raises a `ValueError` exception for the case that either argument is zero, ensuring that the function handles this case properly.