```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input is required")
    elif a == 0 or b == 0:
        return 0
    
    m = max(a, b)
    for i in range(1, m // 2 + 1):
        if a % i == 0 and b % i == 0:
            return i
    
    return m
```