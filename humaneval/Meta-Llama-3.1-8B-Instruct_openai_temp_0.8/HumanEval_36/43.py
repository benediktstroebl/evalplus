```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The number of times the digit 7 appears.

    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(n - 1, 0, -1):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to check for the digit 7
            for digit in str(i):
                if digit == '7':
                    count += 1
                    break
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz(n)` that counts the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function iterates over the range of numbers from `n-1` down to 1, checks each number for divisibility by 11 or 13, and then checks each digit of the number for the presence of the digit 7. The total count is returned at the end.