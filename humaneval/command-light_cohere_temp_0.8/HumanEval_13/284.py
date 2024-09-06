```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    max_ = max(abs(a), abs(b))

    for i in range(1, max_ + 1):
        if a % i == 0 and b % i == 0:
            return i

    return 0
```