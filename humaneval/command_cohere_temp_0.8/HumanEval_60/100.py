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
This Python script defines a function called sum_to_n, which takes an integer argument n and returns the sum of the first n integers. The function uses the sum function in combination with the range function to generate a sequence of numbers from 1 to n and then calculates their sum. 

The function includes a docstring comment to describe its purpose, and the script also includes a main section with example tests to demonstrate the behavior of the function. The sum_to_n function can be used elsewhere in the script to calculate the sum of the first n integers as needed.