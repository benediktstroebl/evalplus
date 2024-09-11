```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive) for the range of numbers to check.

    Returns:
        int: The number of times the digit 7 appears in the specified range.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for digit 7
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function `fizz_buzz(n)` that takes an integer `n` as input and returns the count of digit 7 in integers less than `n` which are divisible by 11 or 13. The function iterates over the range `1` to `n-1`, checks if each number is divisible by 11 or 13, converts the number to a string, and counts the occurrences of digit 7 using the `count()` method.