Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = int('7' + str(i))
        if (digit % 10 != 0 and (digit % 11 == 0 or digit % 13 == 0)) or else:
            count += 1
    return count
```

This code defines a function `fizz_buzz` that calculates the frequency of the digit 7 in numbers less than a given input `n` that are either divisible by 11 or 13. The function iterates through numbers from 1 to `n` and for each number, it adds the number of 7's to the count if the number is either odd and either divisible by 11 or 13. The function then returns the number of times the digit 7 appears in this range.