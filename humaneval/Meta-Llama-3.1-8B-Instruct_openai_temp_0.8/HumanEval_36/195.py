```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper bound (exclusive) for the range of numbers to check.

    Returns:
        int: The number of times the digit 7 appears in the specified range.
    """
    count = 0  # Initialize a counter to store the occurrences of the digit 7
    for i in range(1, n):  # Iterate over all numbers less than n
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_i = str(i)  # Convert the number to a string to easily check for digit 7
            count += str_i.count('7')  # Increment the counter by the number of '7's in the string representation
    return count  # Return the total count of digit 7 occurrences


# Test the function
if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
```

This script uses a simple iterative approach to count the occurrences of the digit 7 in the specified range. It converts each number to a string to easily check for the digit 7 using the `count()` method. The total count is then returned. The script includes docstrings and test cases for clarity and verification.