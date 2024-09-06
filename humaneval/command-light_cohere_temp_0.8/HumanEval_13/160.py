```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be not None")
    return math.sqrt(max(a, b)) if a > b else b
```