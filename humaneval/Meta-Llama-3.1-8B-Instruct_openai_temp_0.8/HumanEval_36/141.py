```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit (exclusive) for the range of numbers to check.
    
    Returns:
    int: The number of times the digit 7 appears in the specified range.
    """
    count = 0
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily access its digits
            str_i = str(i)
            # Count the number of occurrences of '7' in the string representation of the number
            count += str_i.count('7')
    return count


# Test cases
print(fizz_buzz(50)) 
print(fizz_buzz(78))
print(fizz_buzz(79))
```

This script works by iterating over all numbers less than `n`, checking if each number is divisible by 11 or 13, and then counting the occurrences of the digit '7' in the string representation of each such number. The total count of such occurrences is then returned.