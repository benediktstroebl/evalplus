```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = int(str(i)[1])
        if digit % 10 == 7 and ((i % 11 == 0) or (i % 13 == 0)):
            count += 1
    return count

# Test the function
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```
This script defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers that are divisible by 11 or 13 and less than a given integer `n`. The function uses a simple loop to iterate through numbers from 1 to `n`, and counts the occurrences of the digit 7. Additionally, it checks if the numbers are divisible by both 11 and 13 using the modulo operator. The `test_fizz_buzz` function is used to test the `fizz_buzz` function with various input values and ensures the function's correctness.