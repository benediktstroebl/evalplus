```python
def count_sevens(n: int) -> int:
    """
    Count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit.

    Returns:
    int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
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

This script first defines a helper function `count_sevens` that counts the occurrences of the digit 7 in integers less than `n` which are divisible by 11 or 13. It then defines the `fizz_buzz` function which calls `count_sevens` and returns its result. The script also includes test cases to verify the correctness of the `fizz_buzz` function.