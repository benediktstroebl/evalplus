Here is a self-contained Python script that defines a function `fizz_buzz` solving the problem of counting the number of times the digit 7 appears in integers less than a given number `n` which are divisible by 11 or 13:

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
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if digit == '7':
            count += 1
        if count >= 2 and (i % 13 == 0 or i % 11 == 0):
            count = 0
    return count
```

This function iterates through numbers less than or equal to `n`, checks if the current number contains the digit 7, and if it does, the function increments the count. If the count of 7s so far reaches or exceeds 2 and the number is divisible by either 11 or 13, then the count is reset to 0.

You can test the function with the provided test cases or with other values of `n`.