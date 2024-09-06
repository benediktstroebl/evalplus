Here's the function fizz_buzz which counts the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        d = num % 11
        if d == 7:
            count += 1
        d = num % 13
        if d == 7:
            count += 1
    return count
```
This function takes an integer n as input and iterates through numbers less than n. It checks if the ITER is divisible by 11 or 13 and increments the count if the digit 7 is present.