```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be given")
    if a == 0:
        return 0
    if b == 0:
        return 0

    while a != 0:
        b, a = a // b, a

    return max(b, a)
```