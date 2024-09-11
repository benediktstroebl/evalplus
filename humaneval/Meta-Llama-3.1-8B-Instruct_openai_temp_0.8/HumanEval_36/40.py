```python
def count_sevens(n: int) -> int:
    """Count the number of times the digit 7 appears in all integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n - 1, 0, -1):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return count_sevens(n)


# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines two functions. The `count_sevens` function counts the number of times the digit 7 appears in all integers less than `n` which are divisible by 11 or 13. The `fizz_buzz` function calls `count_sevens` to get the desired result. The script includes docstrings for both functions and uses doctests to demonstrate their usage.