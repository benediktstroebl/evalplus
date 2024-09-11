```python
def count_sevens_below_n(n: int) -> int:
    """
    This function counts the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n (int): The upper bound for the range of numbers to check.

    Returns:
        int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper bound for the range of numbers to check.

    Returns:
        int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    return count_sevens_below_n(n)


# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines two functions, `count_sevens_below_n` and `fizz_buzz`. The `count_sevens_below_n` function is a helper function that counts the occurrences of the digit 7 in integers from 0 to `n-1` which are divisible by 11 or 13. The `fizz_buzz` function simply calls `count_sevens_below_n` with the provided argument `n`.