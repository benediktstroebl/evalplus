```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Cannot calculate GCD of zero numbers")
    return math.gcd(a, b)
```