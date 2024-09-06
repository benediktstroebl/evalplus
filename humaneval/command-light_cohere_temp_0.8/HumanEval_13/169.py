```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    if a == b:
        return a
    
    m = max(a, b)
    for i in range(1, int(m**0.5)):
        if m % i == i:
            return i
    
    return m
```