```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit (exclusive) to check for numbers divisible by 11 or 13.

    Returns:
    int: The number of times the digit 7 appears in the specified range.
    """
    count = 0  # Initialize a counter for the digit 7
    for i in range(1, n):  # Iterate over the range from 1 to n (exclusive)
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_i = str(i)  # Convert the number to a string for easier iteration
            count += str_i.count('7')  # Count the occurrences of the digit 7
    return count


# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```