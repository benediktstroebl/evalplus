```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): An integer less than which we need to find the count.

    Returns:
    int: The count of digit 7 in numbers less than n, which are divisible by 11 or 13.
    """
    count = 0
    for i in range(11, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This Python script defines a function `fizz_buzz(n)` that iterates through all integers from 11 to `n-1`, checks if they are divisible by 11 or 13, and then counts the occurrences of the digit 7 in their string representation. The function returns this count.