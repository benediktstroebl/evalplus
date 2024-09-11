```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit (exclusive) of the range to search.
    
    Returns:
    int: The number of times the digit 7 appears in the integers less than n which are divisible by 11 or 13.
    
    Examples:
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(10, n):
        if i % 11 == 0 or i % 13 == 0:
            for digit in str(i):
                if digit == '7':
                    count += 1
                    break
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```
This script defines a function `fizz_buzz(n)` that takes an integer `n` as input, and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It then tests this function with the provided test cases.