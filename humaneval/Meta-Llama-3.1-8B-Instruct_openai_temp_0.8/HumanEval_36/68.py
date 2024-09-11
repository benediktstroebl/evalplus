```python
def count_7_appearances(n: int) -> int:
    """
    Count the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.
    
    Args:
    n (int): Upper limit for the range of numbers to check.
    
    Returns:
    int: The number of times the digit 7 appears in the described integers.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:  # check if the number is divisible by 11 or 13
            # convert the number to a string to easily iterate over its digits
            str_i = str(i)
            for digit in str_i:  # check each digit
                if digit == '7':  # if the digit is 7, increment the count
                    count += 1
    return count


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return count_7_appearances(n)


# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines two functions: `count_7_appearances` and `fizz_buzz`. The `count_7_appearances` function iterates over the numbers less than `n`, checks if each of them is divisible by 11 or 13, and counts the occurrences of the digit 7. The `fizz_buzz` function simply calls `count_7_appearances`. The example usage at the end demonstrates how to use these functions.