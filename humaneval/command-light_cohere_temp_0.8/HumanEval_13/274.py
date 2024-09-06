```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        return 0

    if a == b:
        return a

    for i in range(1, int(a ** 0.5) + 1):
        while b % i == 0:
            a %= i

    return a
```