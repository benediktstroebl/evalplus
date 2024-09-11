```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper bound for checking numbers.

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
    for i in range(11, n, 11):
        str_i = str(i)
        if '7' in str_i:
            count += 1
    for i in range(13, n, 13):
        str_i = str(i)
        if '7' in str_i:
            count += 1
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines a function `fizz_buzz(n)` that counts the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It iterates through the numbers in the given ranges (11 to `n-1` with a step of 11, and 13 to `n-1` with a step of 13), converts each number to a string, and checks if the digit '7' is in the string. If '7' is found, it increments the count. Finally, it returns the count.