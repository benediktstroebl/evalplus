```python
def fizz_buzz(n: int):
    return sum(i for i, digit in enumerate(str(n), 1) if digit == 7 and n % 11 == 0 or n % 13 == 0)

# Test suite
def test():
    assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3

# Example usage
test()
```