```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return math.isqmax(a, b)
```