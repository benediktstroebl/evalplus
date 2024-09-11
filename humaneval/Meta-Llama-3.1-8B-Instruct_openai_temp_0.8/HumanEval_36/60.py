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
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test the function
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
```

This script defines a function `fizz_buzz(n)` that iterates over all integers less than `n`, checks if the integer is divisible by 11 or 13, and counts the occurrences of the digit 7. It then returns the total count. The test cases are included at the end to demonstrate the function's behavior.