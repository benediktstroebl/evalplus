```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    result = []
    while b:
        if b & 1:  # check odd divisor
            result.add(a * a
        b // 2
        b //= 2
    while b:
        if b & 1:  # check even divisor
            result.append(b //
        b // 2
        b //= 2
    
    return max(result) if result else 0
```