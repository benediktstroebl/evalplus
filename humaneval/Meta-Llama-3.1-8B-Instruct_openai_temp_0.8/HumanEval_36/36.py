```python
def count_digit_7(n: int) -> int:
    """
    Count the number of times the digit 7 appears in a number.

    Args:
        num (int): The number to count the digit 7 in.

    Returns:
        int: The number of times the digit 7 appears in the number.
    """
    return str(num).count('7')


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive) to search for numbers.

    Returns:
        int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    return sum(1 for i in range(n) if i % 11 == 0 or i % 13 == 0 and count_digit_7(i) > 0)


# Test cases
print(fizz_buzz(50))  # Should print 0
print(fizz_buzz(78))  # Should print 2
print(fizz_buzz(79))  # Should print 3
```

In this script, the `count_digit_7` function counts the number of times the digit 7 appears in a given number. The `fizz_buzz` function uses a generator expression to iterate over numbers less than the given limit, checks if the number is divisible by 11 or 13, and if it is divisible by either of these numbers, counts the number of times the digit 7 appears in that number. The sum of these counts is then returned.