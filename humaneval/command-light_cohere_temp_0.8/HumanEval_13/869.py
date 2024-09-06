```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the numbers must be a non-zero integer.")
    return math.sqrt(max((a, b)))
```