```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero")
    return max(a, b) / math.mx.floor(max(b, a))
```
Do you require additional help implementing this function?