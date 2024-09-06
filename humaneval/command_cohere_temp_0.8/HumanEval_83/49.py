```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    else: 
        return 2 * ((n * (n + 1)) / 2) - 1
```

The function leverages the formula for calculating the total count of positive integers with `n` digits: `n * (n + 1) / 2`. Subsequently, it adjusts this total to account for double-counting, considering the integers that start and end with 1.

For instance, the integer count for 1-digit numbers is handled correctly by this function:
```python
starts_one_ends(1)
```

This will return `1`, as there is only one 1-digit number that starts and ends with 1: 1.