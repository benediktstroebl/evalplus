```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != 0:
        a, b = divmod(a, b)
        if b == 0:
            break
    
    return b

# Test the function with a few examples
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
>>> greatest_common_divisor(125, 10)
5
>>> greatest_common_divisor(10, 20)
20
```