```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive) to check for numbers divisible by 11 or 13.

    Returns:
        int: The number of times the digit 7 appears in the specified range.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script uses a loop to check each integer in the specified range. If the integer is divisible by 11 or 13 (found using the modulus operator `%`), it converts the integer to a string and uses the `count` method to find the number of occurrences of the digit '7'. The total count of '7' occurrences is then returned.