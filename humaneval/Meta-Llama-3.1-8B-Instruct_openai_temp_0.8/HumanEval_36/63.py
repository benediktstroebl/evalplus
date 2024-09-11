```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The number of occurrences of the digit 7.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            for char in str(i):
                if char == '7':
                    count += 1
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines the `fizz_buzz` function which iterates over all integers less than `n`. For each such integer `i`, it checks if `i` is divisible by either 11 or 13. If it is, the function converts `i` to a string and counts the occurrences of the character '7' in the string. The total count of occurrences of '7' is then returned.

The script also includes test cases as specified in the problem statement.