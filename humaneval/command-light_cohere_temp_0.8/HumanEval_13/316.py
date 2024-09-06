```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Error: Input a or b is empty"
    
    if a == 0:
        return "Error: Input a is zero"
    
    if b == 0:
        return "Error: Input b is zero"
    
    while a % b == 0:
        a //= b
    b //= a
    
    return a
```