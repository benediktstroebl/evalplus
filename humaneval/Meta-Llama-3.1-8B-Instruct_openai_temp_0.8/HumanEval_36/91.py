```python
def fizz_buzz(n: int):
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
    count = 0  # Initialize a counter to store the occurrences of the digit 7
    for i in range(n):  # Iterate over all numbers less than n
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            count += str(i).count('7')  # Convert the number to a string and count the occurrences of '7'
    return count  # Return the total count

# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz(n)` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It uses a loop to iterate over all numbers less than `n`, checks if each number is divisible by 11 or 13, and counts the occurrences of the digit 7 in each number. The total count is then returned.