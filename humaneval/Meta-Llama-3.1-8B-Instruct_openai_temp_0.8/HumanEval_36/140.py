### Fizz Buzz Function
```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit (exclusive).

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

    count = 0  # Initialize count as 0
    for i in range(10, n):  # Iterate over numbers from 10 to n (exclusive)
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_i = str(i)  # Convert the number to string
            count += str_i.count('7')  # Count the occurrences of '7' in the string and add to count

    return count  # Return the count
```
This function works by iterating over numbers from 10 to `n-1` and checking if each number is divisible by 11 or 13. If it is, the function converts the number to a string and counts the occurrences of '7' in the string. The total count of '7' occurrences is then returned.