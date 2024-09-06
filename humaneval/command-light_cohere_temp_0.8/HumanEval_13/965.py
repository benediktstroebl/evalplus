```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs is not provided")
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != 0:
        a, b = divmod(a, b)
        if b == 0:
            break
    
    return b
```