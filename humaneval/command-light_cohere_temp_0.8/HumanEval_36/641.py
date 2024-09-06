Here is a self-contained Python script that defines and implements the function `fizz_buzz` from the prompt:

```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        if int('7' + str(i)) % 10 == 0 and i % 11 == 0 or i % 13 == 0:
            count += 1
    return count
```