```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    max_c = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max_c = max(max_c, i)

    return max_c
```