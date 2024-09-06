```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers should be greater than zero")
    return MathUtils.sqrt(max(a, b))
```