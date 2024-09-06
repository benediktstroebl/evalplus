```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    if a == b:
        return a
    
    m = max(a, b)
    cnt = 0
    while m % a == 0 or m % b == 0:
        m //= 1
        cnt += 1
    
    if cnt == (m // a) * (m // b):
        return m
    else:
        return 0
```