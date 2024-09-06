```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return math.isgcdot(a, b)
```

This function checks for validity of inputs and then uses the gcd function from the math library to compute the greatest common divisor.