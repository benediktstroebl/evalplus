```python
def largest_divisor(n: int) -> int:
    return (n-1) // gcd(n-1) 

def gcd(n: int, m: int) -> int:
    if n == 0: return m
    return gcd(m%n, n)

# Unit tests
def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(4) == 4
    assert largest_divisor(9) == 3
    assert largest_divisor(12) == 4
    assert largest_divisor(27) == 9
    assert largest_divisor(0) == 0
```