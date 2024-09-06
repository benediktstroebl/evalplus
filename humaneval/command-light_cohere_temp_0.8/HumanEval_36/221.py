Here is a Python script with a self-contained function that solves the problem of counting the number of times the digit 7 appears in integers less than a given number n, which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
   >>>
   
    7
    n % 11 == 0 OR n % 13 == 0
    return len([x for x in range(n+1, 0, -1) if x % 11 == 7 or x % 13 == 7])

def test_fizz_buzz():
    """
    Test the fizz_buzz function with various input values and verify the output.
    >>> test_fizz_buzz(50)
    0
    >>> test_fizz_buzz(78)
    2
    >>> test_fizz_buzz(79)
    3
    """
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```
This script defines a function fizz_buzz(n) that calculates the count of 7s in numbers divisible by 11 or 13 from the given integer n. The test_fizz_buzz() function provides test cases to validate the correctness of the fizz_buzz() function.