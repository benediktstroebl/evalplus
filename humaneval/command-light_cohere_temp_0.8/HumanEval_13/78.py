```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    return math.isgcd(a, b)
```
Do you require any other assistance with code?