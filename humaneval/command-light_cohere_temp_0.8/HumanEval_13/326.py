```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Requires both a and b to compute GCD!"
    while b:
        a, b = b, a % b
    return a
```