```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    m = a
    while b != 0:
        a, b = b, a % b
    
    return a

# Test case for function
assert(greatest_common_divisor(3, 5), 1)
assert(greatest_common_divisor(25, 15), 5)
```