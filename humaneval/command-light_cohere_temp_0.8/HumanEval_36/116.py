Here's the self-contained Python script that defines a function `fizz_buzz` which solves the problem you provided earlier:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        if (7) % (i%10) == 0 and ((i%10)!=1) and ((i%100)!=11) and ((i%100)==13):
            count += 1
    return count
```

This function `fizz_buzz` takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function uses a testing in the range from 1 to `n` and checks for the valid conditions for the digit 7 to appear in the corresponding numbers.