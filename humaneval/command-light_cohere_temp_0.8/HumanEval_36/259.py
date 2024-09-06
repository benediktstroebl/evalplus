Here's the code with a self-contained function `fizz_buzz` that calculates the number of times the digit 7 appears in integers less than a given number `n` which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    Returns: 0 if no such 7 appears, otherwise returns the count of how many times 7 appears.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Set up all numbers from 0 to n inclusive
    numbers = [0] + [x for x in range(1, n + 1)]
    
    # Loop through numbers, count occurrences of 7
    for num in numbers:
        if num % 10 == 7:
            count = numbers.remove(num)
        count[:-1]  # to count only first occurrence
    
    return count
```