```python
def count_sevens(n: int) -> int:
    """
    Count the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.

    Args:
    n (int): Upper limit (exclusive) for the range of numbers to check.

    Returns:
    int: The number of times the digit 7 appears in the specified range.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): Upper limit (exclusive) for the range of numbers to check.

    Returns:
    int: The number of times the digit 7 appears in the specified range.
    """
    return count_sevens(n)


# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `count_sevens` that counts the occurrences of the digit 7 in numbers divisible by 11 or 13. It then uses this function to implement the `fizz_buzz` function, which is the original function specified in the problem statement. The script includes test cases to verify its correctness.