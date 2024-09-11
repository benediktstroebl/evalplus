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
    count = 0  # Initialize the count of digit 7
    for i in range(n - 1, 0, -1):  # Iterate from n-1 to 1
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_i = str(i)  # Convert the number to string to check for digit 7
            count += str_i.count('7')  # Increment the count by the number of times '7' appears
    return count  # Return the total count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz(n)` that returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It iterates over the range from `n-1` to 1, checking each number to see if it is divisible by 11 or 13, and if so, it counts the number of times the digit 7 appears in the string representation of the number. Finally, it returns the total count.