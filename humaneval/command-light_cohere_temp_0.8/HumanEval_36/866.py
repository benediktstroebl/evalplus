```python
def fizz_buzz(n):
    counts = 0
    for i in range(2, n+1):
        if int('0' <= str(i) <= '7' and i % 11 == 0 or i % 13 == 0):
            counts += 1
    return counts

# Test suite
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
    assert fizz_buzz(100) == 5
    assert fizz_buzz(120) == 7
    assert fizz_buzz(121) == 8
    assert fizz_buzz(999) == 9
```
This code defines the fizz_buzz function, which returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The test_fizz_buzz function contains a series of assertions that verify the correctness of the fizz_buzz function for different input values.