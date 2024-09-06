```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    m = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            m = i

    return m
```