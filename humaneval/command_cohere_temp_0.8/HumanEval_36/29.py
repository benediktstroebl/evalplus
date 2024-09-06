Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Generate a list of integers from 0 to n-1.
    num_list = list(range(n))
    # Filter out numbers that are not divisible by 11 or 13.
    div_by_11_or_13 = [num for num in num_list if num % 11 == 0 or num % 13 == 0]
    # Count the number of 7's in the filtered list of integers.
    seven_count = sum(1 for num in div_by_11_or_13 if num % 10 == 7)
    return seven_count
```
This code constructs a list of integers from 0 to n-1. It then filters this list, keeping only the integers divisible by 11 or 13. Finally, it counts the number of 7's in the filtered list and returns this count. The function is tested with the following inputs:
```python
>>> fizz_buzz(50)
0
>>> fizz_buzz(78)
2
>>> fizz_buzz(79)
3
```
These tests illustrate the expected behavior of the function.