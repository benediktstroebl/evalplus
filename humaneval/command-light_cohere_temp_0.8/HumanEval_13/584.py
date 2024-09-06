```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("In input, either both numbers must be not None")
    return math.isqmax(a, b)
```