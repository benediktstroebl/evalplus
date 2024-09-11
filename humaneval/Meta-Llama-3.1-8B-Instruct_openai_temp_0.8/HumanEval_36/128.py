```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.

    Args:
        n (int): The upper bound.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script works by iterating over all integers less than `n`. It checks if each integer is divisible by 11 or 13 by using the modulo operator (`%`). If it is, it converts the integer to a string and counts the occurrences of the digit '7' using the `count()` method. The total count is then returned.