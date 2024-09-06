```python
def fizz_buzz(n: int):
    return 7 - sum(map(lambda x: x in str(n), range(10, 0, divisor=11) )))

def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
    assert fizz_buzz(100) == 2
    assert fizz_buzz(10) == 0
    assert fizz_buzz(30) == 2
    assert fizz_buzz(120) == 6
    assert fizz_buzz(121) == 5
```