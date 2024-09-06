```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be not be None.")
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive.")
    return abs(b) if b > a else a
```