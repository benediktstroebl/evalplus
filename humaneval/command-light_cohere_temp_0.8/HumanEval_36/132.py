Here's the Python script with the function `fizz_buzz` that calculates the number of times the digit 7 appears in integers less than a given number `n` that are divisible by 11 or 13:

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
    
    # Count the number of 7s in the range
    count = 0
    for i in range(1, n+1):
        if (7 % i) == 0 and ((11 <= i) or (13 <= i)):
            count += 1

    return count
```
This script provides a clear and self-contained function with a detailed docstring, making it easier to understand and maintain.