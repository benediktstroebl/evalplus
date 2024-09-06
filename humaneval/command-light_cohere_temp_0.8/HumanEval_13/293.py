```python
def greatest_common_divisor(a, b): 
    while b != 0:
        if a % b == 0:
            a, b = b, a
        else:
            b = b //  2
    return a
```