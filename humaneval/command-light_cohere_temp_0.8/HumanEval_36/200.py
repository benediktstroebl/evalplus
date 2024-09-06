Here's the self-contained function that calculates the number of times the digit 7 appears in numbers less than n and divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return sum([1 for x in range(0, n) if int(x) == 7 and x % 11 == 0 or x % 13 == 0])
```
This function uses a list comprehension to count the number of times the digit 7 appears in numbers less than n. It uses the multiple conditions to ensure it only counts numbers that are both less than n and divisible by 11 or 13.