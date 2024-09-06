```python
def fizz_buzz(n: int):
    return {
        7: 0,
        11: 1,
        13: 2,
        9: 3,
        15: 4,
        17: 5,
        19: 6
    }.get(n % 10, 0)

def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
    assert fizz_buzz(101) == 6
    assert fizz_buzz(13) == 1
    assert fizz_buzz(0) == 0
    assert fizz_buzz(60) == 3
```