```python
def count_sevens(n: int) -> int:
    """
    Count the number of times the digit 7 appears in integers less than n
    which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return count_sevens(n)


# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `count_sevens` that counts the occurrences of the digit 7 in numbers that are divisible by 11 or 13. The `fizz_buzz` function calls `count_sevens` with the input number `n`. The example usage at the end demonstrates the function's behavior with the specified test cases.