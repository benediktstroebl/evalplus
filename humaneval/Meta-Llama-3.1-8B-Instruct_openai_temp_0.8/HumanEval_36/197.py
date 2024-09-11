```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The number of times the digit 7 appears in the specified integers.
    """
    count = 0
    for i in range(11, n, 11):  # iterate over numbers divisible by 11
        count += str(i).count('7')
    for i in range(13, n, 13):  # iterate over numbers divisible by 13
        count += str(i).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script uses a simple loop to iterate over numbers less than `n` that are divisible by 11 or 13. For each number, it converts the number to a string and uses the `count` method to count the number of occurrences of the digit '7'. The total count is then returned.