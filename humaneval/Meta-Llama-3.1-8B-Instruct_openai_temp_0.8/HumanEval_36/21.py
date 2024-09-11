```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n (int): The upper limit for the range of numbers to check.
    
    Returns:
        int: The number of times the digit 7 appears in the specified range.
    """
    count = 0  # Initialize a counter to store the number of occurrences of the digit 7
    for i in range(1, n):  # Iterate over the range of numbers from 1 to n-1
        if i % 11 == 0 or i % 13 == 0:  # Check if the current number is divisible by 11 or 13
            str_i = str(i)  # Convert the current number to a string
            count += str_i.count('7')  # Count the occurrences of the digit 7 in the string representation
    return count  # Return the total count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines a function `fizz_buzz(n)` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function iterates over the range of numbers from 1 to `n-1`, checks for divisibility by 11 or 13, and counts the occurrences of the digit 7 in the string representation of each number. The total count is then returned. The script also includes test cases to verify the correctness of the function.