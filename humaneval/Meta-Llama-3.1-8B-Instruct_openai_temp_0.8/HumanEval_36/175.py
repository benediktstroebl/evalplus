```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n (int): An integer.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the presence of '7'
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the count of digit 7 in integers less than `n` which are divisible by 11 or 13. It iterates over all numbers from 1 to `n-1` and checks each one to see if it is divisible by 11 or 13. If it is, it converts the number to a string and counts the number of occurrences of '7' in that string, adding the result to the total count. Finally, it returns the total count. The test cases at the end demonstrate the function's behavior with the specified inputs.