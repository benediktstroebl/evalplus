```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and divisible(n, d)), n)
def divisible(n: int, d: int) -> bool:
    return n % d == 0
def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(6) == 2
    assert largest_divisor(10) == 5
    assert largest_divisor(16) == 4
    assert largest_divisor(28) == 14
    assert largest_divisor(2) == 1
    assert largest_divisor(0) == 0
```