```python
def count_sevens(num: int) -> int:
    """Return the number of times the digit 7 appears in num."""
    return str(num).count('7')


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13."""
    return sum(count_sevens(i) for i in range(n) if i % 11 == 0 or i % 13 == 0)


# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script uses a generator expression to iterate over the range from 0 to `n-1` and filter out numbers that are not divisible by 11 or 13. It then uses the `count_sevens` function to count the occurrences of the digit 7 in each of these numbers and sums up the results to get the total count. The result is returned by the `fizz_buzz` function.