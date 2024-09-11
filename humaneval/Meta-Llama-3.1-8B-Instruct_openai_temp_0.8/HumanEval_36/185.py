```python
def count_sevens(n: int):
    """
    Counts the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit for counting.

    Returns:
    int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n - 1):
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
```

You can run the script using the following code block:
```python
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
```

This script uses a function `count_sevens` to count the occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. It then calls this function from `fizz_buzz` to return the result. The digit count is implemented using the built-in `count` method of the string class in Python. The `count` method returns the number of occurrences of the specified value in the string.