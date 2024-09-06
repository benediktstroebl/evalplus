```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum.

    Returns:
        int: The sum of the first n integers.
    """
    return sum(range(1, n + 1))
```
This Python script defines a function called sum_to_n, which takes an integer argument n and returns the sum of the first n integers starting from 1. It uses the sum function to calculate the sum of the range of integers from 1 to n+1, which includes both the starting and ending numbers, accounting for the fact that the last integer before n+1 is included in the sum. The function is encapsulated with a docstring that describes its purpose, arguments, and return value, providing clarity and documentation for users who utilize the function.