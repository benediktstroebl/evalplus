```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs is invalid: a or b is zero")
    return max(divisor(a), divisor(b))

def divisor(x: int) -> int:
    return x if x > 0 else 0
```