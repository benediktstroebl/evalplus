```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n (int): The upper limit (exclusive) of the range to search in.
    
    Returns:
        int: The number of times the digit 7 appears in the specified range.
    """
    count = 0  # Initialize the count of occurrences of the digit 7
    for i in range(1, n):  # Iterate over the range from 1 to n-1
        if i % 11 == 0 or i % 13 == 0:  # Check if the current number is divisible by 11 or 13
            str_i = str(i)  # Convert the current number to a string for easy digit checking
            count += str_i.count('7')  # Increment the count by the number of occurrences of '7' in the string representation of the current number
    return count  # Return the final count


# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines the `fizz_buzz` function that takes an integer `n` as input and returns the count of occurrences of the digit 7 in integers less than `n` which are divisible by 11 or 13. It then includes test cases to verify the function's correctness.