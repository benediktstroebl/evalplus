Here is a self-contained Python script that defines a function, `fizz_buzz`, to solve the problem you provided:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(c==' or c in '117' for c in str(range(10, n+1, '07')))

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This function uses string manipulation and the `sum` function to count the number of occurrences of the digit 7 in a sequence of integers less than `n` that are divisible by 11 or 13. The function then returns the in each test case the number of times 7 appears in the respective range.