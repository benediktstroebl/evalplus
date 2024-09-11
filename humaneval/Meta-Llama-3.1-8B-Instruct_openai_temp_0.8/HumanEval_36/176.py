```python
def count_sevens(n: int) -> int:
    """
    Count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit (exclusive).

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
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    return count_sevens(n)


# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `count_sevens(n)` that counts the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function `fizz_buzz(n)` simply calls `count_sevens(n)` and returns the result. The test cases at the end verify that the functions work correctly.