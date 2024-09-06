```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b % a, a) + 1
```