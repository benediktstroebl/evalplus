```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and divisible(n, d)), n)

def divisible(n: int, d: int) -> bool:
    return n % d == 0

def test_largest_divisor():
    n = 15
    assert largest_divisor(n) == 5
```