```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("One or both inputs must be a positive integer.")
    return math.floor((math.sqrt(a *b) -sqrt(b) + math.sqrt(a -b))
```