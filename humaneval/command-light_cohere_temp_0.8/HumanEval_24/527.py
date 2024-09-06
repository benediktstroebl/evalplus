```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, int('inf')))

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

largest_divisor(15) # Should return 5
```