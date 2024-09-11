```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): An integer.

    Returns:
        int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Examples:
        >>> fizz_buzz(50)
        0
        >>> fizz_buzz(78)
        2
        >>> fizz_buzz(79)
        3
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count
```

This script defines a function `fizz_buzz(n)` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function uses a loop to iterate over all integers less than `n`, checks whether each integer is divisible by 11 or 13, and increments the count of digit 7 occurrences if it is. The result is returned at the end of the function.