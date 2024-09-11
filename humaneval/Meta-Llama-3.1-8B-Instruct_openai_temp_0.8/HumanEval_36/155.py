```python
def count_sevens(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit for the integers to check.

    Returns:
    int: The count of integers divisible by 11 or 13 that contain the digit 7.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string for easy digit access
            str_i = str(i)
            # Count the occurrences of the digit 7
            count += str_i.count('7')
    return count


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit for the integers to check.

    Returns:
    int: The count of integers divisible by 11 or 13 that contain the digit 7.
    """
    return count_sevens(n)


# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script first defines a helper function `count_sevens` that checks each number below `n` to see if it's divisible by 11 or 13. If it is, it counts the occurrences of the digit 7 in that number. The main function `fizz_buzz` simply calls `count_sevens` and returns the result. The test cases at the end demonstrate the function's behavior.