```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit (exclusive).

    Returns:
    int: The count of digit 7 appearances.

    Examples:
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(n - 1, 0, -1):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count
```

This script defines a function `fizz_buzz(n)` that counts the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It iterates over the range from `n-1` down to 1, checks each number for divisibility by 11 or 13, converts the number to a string, and counts the occurrences of the digit 7. The total count is then returned.