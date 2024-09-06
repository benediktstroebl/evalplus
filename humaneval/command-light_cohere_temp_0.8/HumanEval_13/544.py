```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer")
    return math.gcd(a, b)
```
This Python code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two input numbers `a` and `b`. The function uses the built-in `math.gcd()` function to compute the gcd of two numbers. 
This is a common pattern to reduce the amount of code and increase its readability and maintainability.