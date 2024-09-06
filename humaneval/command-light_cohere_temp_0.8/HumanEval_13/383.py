```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is required")
    if a == 0 or b == 0:
        return 0
    
    gcd = 1
    while b != 0:
        a, b = b, a % b
    gcd = max(gcd, b)
    return gcd
```
Do you have any other questions about Python scripts?