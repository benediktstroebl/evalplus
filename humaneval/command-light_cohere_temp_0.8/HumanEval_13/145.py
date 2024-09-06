```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("Both numbers must be given")
    return math.floor((math.sqrt(max(a, b)) + 1) if a > b else b
```