Here is a self-contained Python script with a function that solves the problem of counting the occurrences of the digit 7 in numbers less than a given input n, which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        num = 0
        while i % 11 == 0 or i % 13 == 0:
            num += 1
            i //= 11 if i % 11 == 0 else 1
        if num == 7:
            count += 1
    return count
```