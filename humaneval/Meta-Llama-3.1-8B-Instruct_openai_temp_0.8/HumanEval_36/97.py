```python
def count_sevens(num: int) -> int:
    """
    Count the number of times the digit 7 appears in the digits of the number.

    Args:
    num (int): The number to count sevens in.

    Returns:
    int: The number of sevens in the digits of the number.
    """
    return str(num).count('7')


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper bound (exclusive).

    Returns:
    int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    return sum(count_sevens(i) for i in range(n) if i % 11 == 0 or i % 13 == 0)


# Test cases
print(fizz_buzz(50))  # Should print 0
print(fizz_buzz(78))  # Should print 2
print(fizz_buzz(79))  # Should print 3
```

This script defines two functions: `count_sevens` which counts the number of times the digit 7 appears in the digits of a number, and `fizz_buzz` which uses the `count_sevens` function to count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The result is then printed for the given test cases.