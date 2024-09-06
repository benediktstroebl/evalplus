```python
def fizz_buzz(n: int) -> int:
    return sum([i in str(n // 11) or i in str(n // 13) for i in range(1, 10)])
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```
This code defines a function **fizz_buzz** that returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The test function **test_fizz_buzz** is provided to check the correctness of the **fizz_buzz** function.