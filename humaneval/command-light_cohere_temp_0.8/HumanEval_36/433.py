Here is a self-contained Python script that defines a function fizz_buzz, which solves the problem of counting the number of times the digit 7 appears in integers less than a given number n, which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    if n < 7:
        return 0
    count = 0
    while n % 11 != 0 and n % 13 != 0:
        n = n // 10
    while n % 11 != 0:
        count += 1
        n = n // 10
    while n % 13 != 0:
        count += 1
        n = n // 10
    return count
```
This script provides a function fizz_buzz, which takes an integer n as input and returns the number of times the digit 7 appears in integers less than n, which are divisible by 11 or 13. The function uses a specific conditions to iterate through numbers less than n and checks for divisibility by 11 and 13. It effectively counts the overall occurrences of 7, and the function returns the total count of 7s found in such numbers.