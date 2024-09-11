```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive) for the range of numbers to check.

    Returns:
        int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0  # Initialize a counter to store the occurrences of the digit 7
    for i in range(11, n, 11):  # Iterate over multiples of 11
        if '7' in str(i):  # Check if the string representation of the number contains '7'
            count += 1
    for i in range(13, n, 13):  # Iterate over multiples of 13
        if '7' in str(i):  # Check if the string representation of the number contains '7'
            count += 1
    return count


# Test the function
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the count of occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. The function iterates over multiples of 11 and 13, converts each number to a string to check for the presence of '7', and increments the counter accordingly. Finally, the script includes test cases to verify the correctness of the function.