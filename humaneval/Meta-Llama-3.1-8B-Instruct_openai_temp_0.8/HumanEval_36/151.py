```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper bound (exclusive) for the numbers to check.

    Returns:
    int: The number of times the digit 7 appears in the specified numbers.

    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function `fizz_buzz` that counts the occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. The function iterates over all numbers less than `n`, checks if they are divisible by 11 or 13, and if so, counts the occurrences of the digit 7 in the string representation of the number. The result is returned at the end.