```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
```