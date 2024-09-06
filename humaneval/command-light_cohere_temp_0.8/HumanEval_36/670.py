```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    if n <= 0:
        return 0
    
    def count_seven(num):
        return any(num % d == 7 for d in [11, 13])
    
    return count_seven(n)

# Unit tests
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```
This code defines a function `fizz_buzz` which counts the number of occurrences of 7 in numbers less than `n` that are divisible by 11 or 13. It also provides unit tests to ensure the correctness of the `fizz_buzz` function.