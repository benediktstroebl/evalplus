```python
def count_digit_7(n: int) -> int:
    """
    Helper function to count the number of times the digit 7 appears in a given integer.

    Args:
    i (int): The integer to count the digit 7 in.

    Returns:
    int: The number of times the digit 7 appears in the integer.
    """
    return str(i).count('7')


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit (exclusive) for the range of integers to check.

    Returns:
    int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    # Initialize a counter for the digit 7
    count = 0
    
    # Iterate over all integers less than n
    for i in range(n):
        # Check if the integer is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Count the occurrences of the digit 7 in the integer
            count += count_digit_7(i)
    
    return count

# Test cases
print(fizz_buzz(50))  # Should print 0
print(fizz_buzz(78))  # Should print 2
print(fizz_buzz(79))  # Should print 3
```

This script defines two functions: `count_digit_7` to count the occurrences of the digit 7 in a given integer and `fizz_buzz` to find the total occurrences of the digit 7 in integers less than `n` which are divisible by 11 or 13. The result is then printed for the test cases.