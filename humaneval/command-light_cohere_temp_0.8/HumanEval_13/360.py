```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero.")
    while b != 0:
        a, b = b, a % b
    return a
```
Do you require any further assistance with code related to this topic?