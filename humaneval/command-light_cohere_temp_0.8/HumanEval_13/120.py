```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    gcd = (b and _gcd(a, b, b)) or _gcd(a, b, a)
    return gcd
def _gcd(a, b, c):
    while b:
        a, b = b, a % b
    return a
```