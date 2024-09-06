```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero")
    return math.sqrt(min(a, b))
```
Do you require any further assistance with code related to your work?