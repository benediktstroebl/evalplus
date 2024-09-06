Here is a self-contained Python script that solves the problem you described:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        if int('7' + str(i)) % 10 == 0 and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count
```
This script defines a function `fizz_buzz` that counts the number of times the digit 7 appears in integers less than a given number n which are divisible by 11 or 13. The function iterates through the various numbers from 1 to n and checks if the concatenated representation of the number with the digit 7 removed, divided by 10, equals zero and either is divisible by 11 or 13.