```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The number of occurrences of the digit 7.

    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0  # Initialize a counter for the occurrences of 7
    for i in range(n):  # Iterate over all integers less than n
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_i = str(i)  # Convert the number to a string
            count += str_i.count('7')  # Count the occurrences of 7
    return count  # Return the total count

# Test the function
print(fizz_buzz(50))  # Should print 0
print(fizz_buzz(78))  # Should print 2
print(fizz_buzz(79))  # Should print 3
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function iterates over all integers less than `n`, checks for divisibility by 11 or 13, and counts the occurrences of 7 in the string representation of each number. The total count is then returned.