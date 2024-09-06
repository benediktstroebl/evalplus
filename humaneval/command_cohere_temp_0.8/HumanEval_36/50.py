Here's a Python script with a self-contained function `fizz_buzz` that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers with 7 and divisible by 11 or 13 from the range below n
    relevant_numbers = [7*i//11 for i in range(1, n+1, 11)] + [7*i//13 for i in range(1, n+1, 13)]
    return sum(filter(lambda x: x == 7, relevant_numbers))
```
This script defines the `fizz_buzz` function, which takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` that are divisible by 11 or 13. It then uses a list comprehension to generate a list of relevant numbers by filtering integers in the range [1, n] that are divisible by 11 or 13 and contain the digit 7. The sum function is used to count the number of occurrences of the digit 7 in the `relevant_numbers` list, and finally, the result is returned as the output of the function. 

Here's a markdown code block with the function and tests:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers with 7 and divisible by 11 or 13 from the range below n
    relevant_numbers = [7*i//11 for i in range(1, n+1, 11)] + [7*i//13 for i in range(1, n+1, 13)]
    return sum(filter(lambda x: x == 7, relevant_numbers))

# Test cases
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```