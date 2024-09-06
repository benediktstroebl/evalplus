```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("Both numbers must be provided")
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both numbers must be integers")

    if a == 0:
        return b
    elif b == 0:
        return a

    while a != 0:
        a, b = b % a, a

    return min(a, b)
```