Here's a self-contained Python function that solves the problem you described: 

```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        num = 10 * i
        if (num % 11 == 0 or num % 13 == 0) and num < n:
            count += num // 10
    return count
``` 
This code defines a function called `fizz_buzz` that aims to solve the problem you provided. It counts by counting the accuracy, the number of times the digit 7 appears in integers less than `n` that are divisible by 11 or 13.