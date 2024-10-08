```python
def count_sevens(n: int) -> int:
    """
    Counts the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.
    
    Args:
        n (int): The upper limit for the range of numbers to check.
    
    Returns:
        int: The count of numbers less than n which are divisible by 11 or 13 and contain the digit 7.
    """
    count = 0
    for i in range(n):
        # Check if the current number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the digit 7
            str_i = str(i)
            # Check if the digit 7 appears in the string representation of the number
            if '7' in str_i:
                count += 1
    return count


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n (int): The upper limit for the range of numbers to check.
    
    Returns:
        int: The count of numbers less than n which are divisible by 11 or 13 and contain the digit 7.
    """
    return count_sevens(n)


# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines a helper function `count_sevens(n)` that counts the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The `fizz_buzz(n)` function simply calls `count_sevens(n)` to achieve the same result. The script then includes test cases to verify the correctness of the implementation.