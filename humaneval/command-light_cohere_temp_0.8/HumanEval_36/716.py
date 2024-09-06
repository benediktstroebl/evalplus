```python
def fizz_buzz(n: int) -> int:
    return sum([7] * c for c in range(2, n+1) if c % 11 or c % 13 == 0)

# Test suite
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```
This code defines a function fizz_buzz that calculates the number of occurrences of the digit 7 in numbers less than a given number n, specifically those that are divisible by 11 or 13. The function uses a summation to count these digits and returns the result.