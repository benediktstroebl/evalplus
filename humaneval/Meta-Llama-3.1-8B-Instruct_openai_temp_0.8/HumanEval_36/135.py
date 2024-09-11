### Fizz Buzz Problem Solver
#### Problem Statement
Return the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.

#### Python Solution
```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit of the range.

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
    count = 0
    for i in range(n - 1, 0, -1):  # Start from n-1 and go down to 1
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_i = str(i)  # Convert the number to a string to easily access its digits
            count += str_i.count('7')  # Count the occurrences of the digit 7
    return count
```

You can run this script in a Python environment to test the `fizz_buzz` function.