```python
def count_sevens(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n - 1, 1, -1):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_sevens(n)


# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `count_sevens(n)` that counts the number of occurrences of the digit 7 in integers less than `n` which are divisible by 11 or 13. It does this by iterating over the integers from `n-1` down to 2 (since we start counting from 2, not 1), checking if the current integer is divisible by 11 or 13, and if so, counting the occurrences of '7' in its string representation.

The function `fizz_buzz(n)` simply calls `count_sevens(n)` to perform the actual counting.

The test cases at the end of the script verify that the functions behave as expected.