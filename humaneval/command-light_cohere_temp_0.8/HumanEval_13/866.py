```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs is invalid: a or b must be greater than 0")
    return math.gcd(a, b)
```