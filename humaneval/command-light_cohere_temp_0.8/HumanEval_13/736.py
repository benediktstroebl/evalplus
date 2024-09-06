```python
def greatest_common_divisor(a, b): 
    while b != 0:
        c = b
        b = a % b
    return c
```