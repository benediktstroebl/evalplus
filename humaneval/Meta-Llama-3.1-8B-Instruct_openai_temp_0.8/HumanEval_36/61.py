```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper bound of the range of integers to check.

    Returns:
    int: The number of times the digit 7 appears in the specified range.
    """
    count = 0
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily count the occurrences of '7'
            count += str(i).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This Python script defines a function `fizz_buzz(n)` that counts the occurrences of the digit 7 in integers less than `n` which are divisible by 11 or 13. The function iterates over the range of integers from 0 to `n-1`, checks if each number is divisible by either 11 or 13, and counts the occurrences of '7' in the number's string representation. The count is then returned as the result.