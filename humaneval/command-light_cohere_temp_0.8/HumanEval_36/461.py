```python
def fizz_buzz(n: int):
    return sum([i in str(i) for i in range(1, n+1) if i % 11 or i % 13 == 7])

#Test the function
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```
This Python script defines a function fizz_buzz that counts the number of occurrences of the digit 7 in numbers that are less than n and are divisible by 11 or 13. The function returns the test_fizz_buzz function which checks the outputs of fizz_buzz against the expected results for the test inputs 50, 78, and 79, and asserts that they are correct.