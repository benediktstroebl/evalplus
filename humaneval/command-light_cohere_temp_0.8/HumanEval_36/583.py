Here's the self-contained Python script with the function `fizz_buzz` that counts the number of times the digit 7 appears in integers less than a given number `n` which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    >>> fizz_buzz(1)
    0
    >>> fizz_buzz(130)
    6
    >>> fizz_buzz(156)
    3
    >>> fizz_buzz(0)
    0
    """

    # Define a mapping of numbers divisible by 11 or 13 to the number 7
    mod11_13_map = {7: 0}

    for num in range(n, 0, -1):
        # Check if num is divisible by 11 or 13
        if num % 11 == 0 or num % 13 == 0:
            # Update the mapping with num
            mod11_13_map[num] = 7
        # If 7 is not in the mapping, then it appeared once
        if 7 in mod11_13_map:
            return 1

    # If 7 did not appear in the numbers less than n, then it appeared 0 times
    return 0
```

The function iterates through numbers less than `n` and checks if they are divisible by 11 or 13. If a number is divisible by 11 or 13, then it updates the mapping with that number, if 7 is not in the mapping, it adds 1 to the counter for the times 7 appeared. If 7 did not appear in any of the numbers, it returns 0.