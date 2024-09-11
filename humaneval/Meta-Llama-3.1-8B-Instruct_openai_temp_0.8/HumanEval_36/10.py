```markdown
### Fizz Buzz Digit Count
#### Solution

This script defines a function `fizz_buzz` that counts the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.

```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The count of digit 7.

    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string for digit checking
            str_i = str(i)
            # Count the occurrences of the digit 7
            count += str_i.count('7')
    return count

# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script uses a simple loop to iterate over numbers less than `n` and checks if each number is divisible by 11 or 13. If it is, it converts the number to a string and counts the occurrences of the digit 7. The total count is then returned.