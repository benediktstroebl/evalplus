```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    if a == b:
        return a
    
    # Start from larger divisor and reduce
    max_divisor = max(a, b)
    while max_divisor % max_divisor == 0:
        max_divisor += 1
    
    return max_divisor
```