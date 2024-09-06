```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not operator.isdigit(d) orrem(n, d) == 0) or d == n)

#unit tests
def test_largest_divisor():
    assert largest_divisor(15) == 5
 assert largest_divisor(20) == 4
 assert largest_divisor(25) == 5
 assert largest_divisor(30) == 5
 assert largest_divisor(50) == 10
 assert largest_divisor(55) == 11
 assert largest_divisor(100) == 50
```