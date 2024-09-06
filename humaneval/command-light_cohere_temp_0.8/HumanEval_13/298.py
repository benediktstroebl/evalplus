```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both inputs must be positive numbers")
    while b != 0:
        a, b = b, a % b
    return a
```