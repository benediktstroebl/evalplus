```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of inputs must be a positive integer")
    return math.sqrt(min(a, b))
```