```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.

    Args:
    n (int): The upper limit (exclusive).

    Returns:
    int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the digit 7
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function iterates over all numbers less than `n`, checks if each number is divisible by 11 or 13, and counts the number of times the digit 7 appears in each such number. The result is then returned. The script also includes test cases to verify the correctness of the function.