```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs is invalid: a or b is zero")
    return math.floor((math.sqrt(a * b + math.sqrt(b)) / math.sqrt(a)) if a >= 2
```