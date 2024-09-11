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
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

In this script, we iterate over all integers less than `n`, and for each integer, we check if it is divisible by either 11 or 13. If it is, we count the occurrences of the digit '7' in the string representation of the integer. Finally, we return the total count.