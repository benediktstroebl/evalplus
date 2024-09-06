Here's a Python script with a self-contained function `fizz_buzz` that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers less than n, include only those divisible by 11 or 13
    relevant_numbers = [i for i in range(n + 1)] if (i % 11 == 0 or i % 13 == 0) else []
    # Count occurrences of digit 7 in the filtered list
    sevens_count = sum(1 for num in relevant_numbers if num % 10 == 7)
    return sevens_count
```

This script defines the `fizz_buzz` function, which takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` that are divisible by 11 or 13. This function relies on two underpinning concepts:
1. Filtering Out Relevant Numbers: The function employs a list comprehension to sift through the integers from `1` to `n`, excluding those that are not divisible by 11 or 13.
2. Digit Counting: The function then counts the number of 7s in the subset of numbers, a task facilitated by another list comprehension, which operates over the filtered list of relevant numbers.

The total count of 7s, dispersed amongst the relevant numbers, is returned as the output of this function.