Here's the self-contained Python script with a function `fizz_buzz` that calculates the number of times the digit 7 appears in integers less than a given number `n` which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    if n <= 0:
        return 0
    
    def count_7s(num):
        return any(map(lambda x: x == 7, num)) + \
               (num % 10 == 7) * ((n % 13 == 0) or count_7s(num // 10))
    
    return count_7s(n)

# Unit tests
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```
This script defines the `fizz_buzz` function that calculates the number of occurrences of the digit 7 in numbers less than `n` which are divisible by 11 or 13. The function also includes a unit tests to ensure the correctness of the `fizz_buzz` function with different input values.