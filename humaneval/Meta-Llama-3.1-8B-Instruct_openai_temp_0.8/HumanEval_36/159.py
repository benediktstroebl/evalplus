```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit (exclusive) for checking numbers.

    Returns:
    int: The count of numbers containing the digit 7.
    """
    count = 0  # Initialize count variable to 0
    for i in range(1, n):  # Iterate over numbers from 1 to n-1
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_i = str(i)  # Convert the number to a string for easier digit checking
            count += str_i.count('7')  # Count the occurrences of '7' in the string representation
    return count  # Return the total count


# Test the function
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines the `fizz_buzz` function, which iterates over numbers less than the input `n`, checks if each number is divisible by 11 or 13, and counts the occurrences of the digit 7 in each such number. The function then returns the total count. The test cases at the end demonstrate the function's correctness.