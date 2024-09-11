```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): An integer.

    Returns:
        int: The number of times the digit 7 appears.

    Examples:
        >>> fizz_buzz(50)
        0
        >>> fizz_buzz(78)
        2
        >>> fizz_buzz(79)
        3
    """
    count = 0
    for i in range(11, n, 11):
        for digit in str(i):
            if digit == '7':
                count += 1
    for i in range(13, n, 13):
        for digit in str(i):
            if digit == '7':
                count += 1
    return count
```

This script uses nested loops to iterate over numbers below `n` that are divisible by 11 or 13, converts the numbers to strings to easily check each digit, and increments a counter when the digit 7 is found. The final count is returned as the result of the function.