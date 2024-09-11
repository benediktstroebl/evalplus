```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive) for the range of numbers to check.

    Returns:
        int: The number of times the digit 7 appears in the specified range.

    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz(n)` that checks all integers less than `n` to see if they are divisible by 11 or 13. If they are, it then checks each digit of the integer to see if it is 7. The function returns the total count of these occurrences. The script then prints out the results of the function for the specified test cases.