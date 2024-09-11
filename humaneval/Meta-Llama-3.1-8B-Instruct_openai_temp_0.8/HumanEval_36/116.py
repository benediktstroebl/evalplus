### Fizz Buzz Script
```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The count of digit 7 in the specified range.

    Example:
        >>> fizz_buzz(50)
        0
        >>> fizz_buzz(78)
        2
        >>> fizz_buzz(79)
        3
    """
    count = 0
    for i in range(11, n, 11):
        for digit in str(i):
            if digit == '7':
                count += 1
    for i in range(13, n, 13):
        for digit in str(i):
            if digit == '7':
                count += 1
    return count
```
This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the count of digit 7 in integers less than `n` which are divisible by 11 or 13. The function iterates over the numbers in the specified range, converts each number to a string, and checks each digit for equality with '7'. The count of such occurrences is returned at the end.