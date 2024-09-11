```markdown
# Fizz Buzz Counter
====================

A Python script to count the occurrences of the digit 7 in integers less than `n` which are divisible by 11 or 13.

```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive) to search for numbers.

    Returns:
        int: The count of numbers divisible by 11 or 13 that contain the digit 7.
    """
    count = 0
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the digit 7
            str_i = str(i)
            # Count the occurrences of the digit 7
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz(n)` that takes an integer `n` as input and returns the count of numbers less than `n` that are divisible by 11 or 13 and contain the digit 7. The function iterates over the range from 0 to `n-1`, checks each number for divisibility by 11 or 13, and if it is, converts the number to a string to easily count the occurrences of the digit 7. The final count is returned by the function. The script includes test cases to demonstrate its correctness.