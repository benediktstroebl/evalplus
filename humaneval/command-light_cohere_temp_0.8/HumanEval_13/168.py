```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input is required")
    if a == 0 or b == 0:
        return 0
    
    # Find the greatest divisor of a and b
    gcd = []
    while a != 0 and b != 0:
        t = a % b
        a, b = b, a
    gcd.v = t
    max(gcd)
    return gcd[0]
```