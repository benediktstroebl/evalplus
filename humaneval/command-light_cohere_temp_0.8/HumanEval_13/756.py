```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("One or both inputs cannot be empty")
    return math.gcd(a, b)
```
Do you need help with anything else?