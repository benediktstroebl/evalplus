```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive.")
    return math.gcd(a, b)
```
This function returns the greatest common divisor of a and b, and raises an error if the inputs are not valid.