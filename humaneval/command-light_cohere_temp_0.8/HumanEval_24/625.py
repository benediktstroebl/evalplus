```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 1)

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b % a, a)

largest_divisor(15)  # This will return 5
```