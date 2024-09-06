```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Input must be numbers")
    return math.sqrt(max(a, b))
```