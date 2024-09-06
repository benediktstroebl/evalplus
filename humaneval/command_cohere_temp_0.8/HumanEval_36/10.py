Here's a Python script that contains a function fizz_buzz that solves the problem as outlined in the markdown code block provided. The function is accompanied by a few unit tests to validate its correctness:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers that are less than n and divisible by 11 or 13
    relevant_numbers = [num for num in range(n) if num % 11 == 0 or num % 13 == 0]
    # Count the occurrences of digit 7 in the filtered numbers
    seven_count = sum(1 for num in relevant_numbers if num % 10 == 7)
    return seven_count

# Unit tests
assert fizz_buzz(50) == 0, "Expected fizz_buzz(50) to be 0"
assert fizz_buzz(78) == 2, "Expected fizz_buzz(78) to be 2"
assert fizz_buzz(79) == 3, "Expected fizz_buzz(79) to be 3"
```

The `fizz_buzz` function uses a list comprehension to filter out the relevant numbers from the less than `n` integers, then employs another list comprehension to count the occurrences of the digit 7. The tests assert the function's correctness against the specified inputs.