```python
def largest_divisor(n: int) -> int:
    return (n-1) // gcd(n-1)
def gcd(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x
# Test the function
assert largest_divisor(15) == 5
```