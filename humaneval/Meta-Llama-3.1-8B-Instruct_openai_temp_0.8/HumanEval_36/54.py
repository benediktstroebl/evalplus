```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit (exclusive) for the range of numbers to check.
    
    Returns:
    int: The count of numbers less than n that are divisible by 11 or 13 and contain the digit 7.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            if '7' in str_i:
                count += 1
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script iterates over all integers less than `n` that are divisible by 11 or 13, converts each integer to a string, checks if the string contains the digit '7', and increments a counter if it does. Finally, it returns the total count.