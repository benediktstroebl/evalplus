```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the numbers must be greater than zero.")
    return math.gcd(a, b)
```