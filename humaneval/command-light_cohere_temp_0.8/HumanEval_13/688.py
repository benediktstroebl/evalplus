```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max(x for x in range(1, max(a, b)) if all(d % x == 0 for d in (a, b)))
```