```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive) for the range of integers to check.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

# Example use cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script works by iterating over all integers less than `n`, checking if the integer is divisible by 11 or 13, and if so, counting the number of occurrences of the digit 7 in the string representation of the integer. The `count('7')` method of the string returns the number of occurrences of the substring '7'. The total count across all such integers is then returned.