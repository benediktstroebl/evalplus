```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    if a == b:
        return a

    max_len = max(len(map(int, str(a))), len(str(b)))
    for div in range(1, max_len + 1):
        if a % div == 0 and b % div == 0:
            continue
    
    return a + b
```