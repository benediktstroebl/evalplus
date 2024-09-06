```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    return max(divisor(a) ,divisor(b))

def divisor(x):
    if x == 1:
        return 0
    return x
```