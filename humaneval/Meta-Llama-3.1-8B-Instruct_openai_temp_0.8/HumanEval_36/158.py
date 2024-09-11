```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The number of times the digit 7 appears.

    Examples:
        >>> fizz_buzz(50)
        0
        >>> fizz_buzz(78)
        2
        >>> fizz_buzz(79)
        3
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the presence of '7'
            str_i = str(i)
            # Count the number of occurrences of '7' in the string
            count += str_i.count('7')
    return count

# Test the function
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function uses a loop to iterate over all integers less than `n`, checks if each number is divisible by 11 or 13, and counts the occurrences of the digit 7 in the string representation of each number. The function finally returns the total count.