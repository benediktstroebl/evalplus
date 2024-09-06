```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    if a == b:
        return 1

    m = max(a, b)
    i = 2
    while i * i <= m:
        if a % i == 0 and b % i == 0:
            return i
        i += 1

    return m
```