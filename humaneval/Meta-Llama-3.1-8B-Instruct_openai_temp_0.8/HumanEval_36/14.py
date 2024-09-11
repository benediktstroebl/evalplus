```python
def count_sevens(n: int):
    """
    Helper function to count the number of times the digit 7 appears in a number.
    """
    return str(n).count('7')


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Count the occurrences of the digit 7 in the number
            count += count_sevens(i)
    return count


# Example usage:
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script uses a `count_sevens` helper function to count the occurrences of the digit 7 in a number, and then uses this function in the `fizz_buzz` function to count the occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13.