```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Cannot calculate GCD, both numbers must be positive")
    return math.isq(a, b)
```