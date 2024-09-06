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
This code defines a Python function called `sum_to_n` that takes a single argument `n`, which is an integer representing the number of integers to sum. Inside the function, it uses the `sum` function in combination with the `range` function to calculate the sum of the first 'n' integers. The `range` function generates a sequence of numbers starting from 1 up to 'n', and the `sum` function adds up all the values in this sequence, giving you the sum of the first 'n' integers. The result is then returned as the output of the function. 

The function includes a docstring with documentation that explains its purpose, arguments, and return value, making it easier for developers to understand and utilize the function effectively.

This solution is efficient and can handle large values of 'n' due to the use of the `range` function, which generates values only as needed and avoids the need to store a large list of numbers in memory.