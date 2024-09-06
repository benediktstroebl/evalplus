```python
def fizz_buzz(n):
    return 7 - sum(1 for d in range(2, n+1) if any(d % 11 == 7) or d % 13 == 7)

# Test suite
def test():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
    assert fizz_buzz(100) == 6
    assert fizz_buzz(129) == 5
    assert fizz_buzz(271) == 8
    assert fizz_buzz(50 + 78 + 71) == 0
```