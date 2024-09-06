```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    if a == b:
        return a
    
    m = min(a, b)
    for d in range(1, int(m ** 0.5)):
        if d * m == 0:
            return d
```