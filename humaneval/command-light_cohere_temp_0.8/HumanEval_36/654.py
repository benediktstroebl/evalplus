Here is a self-contained Python script that defines a function fizz_buzz that computes and returns the number of times the digit 7 appears in numbers less than n which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    counts = 0
    for num in range(1, n+1):
        num = str(num)
        if (num[0] == 7) and ((num[1] >= 1) or (num[1] <= 4)):
            counts += 1  
    return counts
```