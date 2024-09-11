```python
def count_sevens(n: int) -> int:
    """
    Count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit for the search.
    
    Returns:
    int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the digit 7
            str_i = str(i)
            # Count the number of times the digit 7 appears
            count += str_i.count('7')
    return count

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return count_sevens(n)

# Test the function
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines a helper function `count_sevens` to count the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. Then it defines the `fizz_buzz` function which simply calls `count_sevens`. The `fizz_buzz` function is tested at the end with the provided test cases.