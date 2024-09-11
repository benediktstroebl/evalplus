```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.

    Args:
    n (int): The upper limit.

    Returns:
    int: The number of times the digit 7 appears.
    """

    def appears_in_divisible(n, digits):
        """Check if the digit appears in the given digits."""
        for digit in digits:
            if str(digit) in str(n):
                return True
        return False

    # Use a generator expression to filter the numbers that meet the conditions
    count = sum(
        1
        for i in range(1, n)
        if (i % 11 == 0 or i % 13 == 0) and appears_in_divisible(i, [7])
    )
    return count
```

You can test this function with the provided examples:
```python
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function `fizz_buzz` that counts the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It uses a helper function `appears_in_divisible` to check if a digit appears in a given number. The main function uses a generator expression to iterate over the numbers and count the ones that meet the conditions.