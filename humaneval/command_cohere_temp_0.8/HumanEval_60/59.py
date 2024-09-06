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
This code defines a Python function called `sum_to_n` that takes a single argument `n`, which is an integer representing the number of integers to sum. Inside the function, it uses the `sum` function in combination with the `range` function to calculate the sum of the first `n` integers. The `range` function generates a sequence of numbers starting from 1 up to `n`, and the `sum` function adds up all the elements in this sequence, giving you the sum of the first `n` integers. Finally, it returns this calculated sum as an integer value. 

The function is documented with a docstring that explains its purpose, parameters, and return value, making it easier for developers to understand and use the function correctly. 

You can use this function to calculate the sum of the first `n` integers by passing different values for `n` when calling the function.