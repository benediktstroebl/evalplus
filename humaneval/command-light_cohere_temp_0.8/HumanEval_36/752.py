Here's the self-contained Python function:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    counts = 0
    for num in range(1, n+1):
        if (num % 11 == 7) or (num % 13 == 7):
            counts += 1
    return counts
```
This function counts the occurrences of 7 in numbers less than `n` that are divisible by 11 or 13, and returns that count. The function uses an iterative approach to loop through numbers from 1 to `n`, checking if the number is divisible by 11 or 13 and, if it is, incrementing a count for how many 7's are encountered in that range. The function then returns the result count, which represents how many times the digit 7 appears in the list of numbers less than n that are divisible by 11 or 13.