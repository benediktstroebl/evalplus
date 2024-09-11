```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit.

    Returns:
    int: The number of times the digit 7 appears.

    Examples:
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0  # Initialize a counter to store the number of times the digit 7 appears
    for i in range(2, n):  # Iterate through integers from 2 to n-1
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_i = str(i)  # Convert the number to a string
            count += str_i.count('7')  # Increment the counter by the number of times '7' appears in the string
    return count  # Return the total count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It uses a loop to iterate through integers from 2 to `n-1`, checks if each number is divisible by 11 or 13, converts each number to a string, and increments a counter by the number of times '7' appears in the string. Finally, it returns the total count. The script also includes test cases to demonstrate its correctness.