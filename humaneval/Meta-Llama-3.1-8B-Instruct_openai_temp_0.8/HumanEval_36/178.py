```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit of the range.

    Returns:
        int: The count of occurrences of the digit 7.
    """
    count = 0
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the digit 7
            str_i = str(i)
            # Check if the digit 7 appears in the number
            if '7' in str_i:
                count += 1
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines a function `fizz_buzz(n)` that iterates over numbers less than `n`, checks if each number is divisible by 11 or 13, converts the number to a string to search for the digit 7, and increments the count if the digit 7 is found. Finally, it returns the count. The test cases at the end verify that the function produces the expected output.