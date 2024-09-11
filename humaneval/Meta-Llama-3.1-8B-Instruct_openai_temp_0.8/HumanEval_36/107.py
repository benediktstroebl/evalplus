### Fizz Buzz Problem Solution
```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The number of times the digit 7 appears.

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

This script defines a function `fizz_buzz` that iterates over all integers less than `n`, checks if they are divisible by 11 or 13, and counts the occurrences of the digit 7 in each number. The function returns the total count.

You can call the function with a specific number to get the count, like this: `print(fizz_buzz(50))`