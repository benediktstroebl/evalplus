```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not divisible(n, d)))

def divisible(n: int, d: int) -> bool:
    return n % d == 0

def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(10) == 5
    assert largest_divisor(4) == 2
    assert largest_divisor(16) == 8
    assert largest_divisor(27) == 13
    assert largest_divisor(9) == 3
    assert largest_divisor(21) == 7
    assert largest_divisor(125) == 25
```