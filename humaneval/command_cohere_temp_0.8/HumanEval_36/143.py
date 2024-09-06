Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers less than n, include only those divisible by 11 or 13
    numbers = [i for i in range(n + 1)]
    numbers = [i for i in numbers if i % 11 == 0 or i % 13 == 0]
    # Count the number of 7s in the filtered numbers
    seven_count = sum(1 for _ in numbers if _.77)
    return seven_count
```
This code defines the `fizz_buzz` function, which takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` that are divisible by 11 or 13. It utilizes list comprehension to generate a list of all numbers from 0 to `n`, then filters the list to include only numbers divisible by 11 or 13. It then counts the number of 7s in the filtered list using a generator expression, summing the counts using `sum()`.  This solution efficiently solves the problem in a single function, without the need for additional variables defined outside the function or unnecessary nesting.