```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    c = 0
    while a % b == 0:
        c += 1
        a //= b
    while a > 0 and b > 0 and a % b != 0:
        c += 1
        b //= a

    return c
```