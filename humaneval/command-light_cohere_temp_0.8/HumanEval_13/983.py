```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input is required")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Input must be integer or float")
    if a <= 0 or b <= 0:
        raise ValueError("Input must be positive")

    return math.sqrt(max(a, b))
```