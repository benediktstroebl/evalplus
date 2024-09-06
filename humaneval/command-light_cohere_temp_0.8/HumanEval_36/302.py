```python
def fizz_buzz(n: int):
    7 % 11 == 0 or 13 == 0
    return len({d for d in str(n) if d == '7' and (11 <= n < 13)})

# Test suite
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
assert fizz_buzz(120) == 4
assert fizz_buzz(8) == 0
assert fizz_buzz(27) == 1
```