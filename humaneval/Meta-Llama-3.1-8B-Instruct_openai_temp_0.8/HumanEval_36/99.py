```python
def count_sevens(n: int) -> int:
    """
    Returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit.

    Returns:
    int: The count of digit 7.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return count_sevens(n)

# Test the function
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```
In this script, the `count_sevens` function iterates over the numbers less than `n`, checks if they are divisible by 11 or 13, converts them to strings, and counts the occurrences of the digit 7. The `fizz_buzz` function simply calls `count_sevens`.