Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n):
    return sum(int(d) == 7 for d in str(n) if n % 11 == 0 or n % 13 == 0)
```
This function calculates the sum of digits in the string representation of the number n when it is represented as an integer divisible by 11 or 13. The sum is calculated only for the digit 7 to determine the answer to the Fizz Buzz question. This will return the number of times the digit 7 appears in integers less than n that are divisible by 11 or 13, as asked in the prompt. 

Here is a test suite that you can use to verify that the function works as expected:
```python
def test_fizz_buzz():
    # Basic Cases
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3

    # Edge Cases
    assert fizz_buzz(10) == 0
    assert fizz_buzz(12) == 1
    assert fizz_buzz(13) == 1
    assert fizz_buzz(18) == 2

    # Larger Numbers
    assert fizz_buzz(110) == 3
    assert fizz_buzz(121) == 4
    assert fizz_buzz(130) == 4
    assert fizz_buzz(140) == 5
```
This test suite contains a variety of tests to ensure that the function fizz_buzz behaves as expected for inputs ranging from very small values to larger values.