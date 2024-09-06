```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    if a == 0:
        return 0
    if b == 0:
        return 0

    while a % b == 0:
        a //= b
    elif a == b:
        return a
    else:
        return 0
```