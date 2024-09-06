```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs is not a number.")
    return math.sqrt(max((a % b, 0)))
```