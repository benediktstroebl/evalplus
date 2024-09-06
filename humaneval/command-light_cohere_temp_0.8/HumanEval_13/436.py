```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "One or both arguments must be numbers"
    while a != 0:
        b = b % a
    return b
```