```python
def fizz_buzz(n: int):
    return 7 - (n // 13) if n % 13 != 0 else 7 + (n // 11)

# Unit tests
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```