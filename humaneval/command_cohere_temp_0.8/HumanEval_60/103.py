```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum

    Returns:
        int: The sum of the first n integers
    """
    return sum(range(1, n + 1))
```

This code defines a function called `sum_to_n` that takes an integer argument `n`. It returns the sum of the first `n` integers from 1 to `n` inclusive. This is achieved using Python's `range` function which creates a sequence of numbers from 1 to `n` and the `sum` function which adds all elements in this sequence. 

The function's docstring provides documentation, explaining its purpose, parameters, and return value. 

To test this function, you can call it with different values of `n` and compare the output with the expected results:
```python
# Test case with sum_to_n(30)
assert sum_to_n(30) == 465

# Test case with sum_to_n(100)
assert sum_to_n(100) == 5050

# Test case with sum_to_n(5)
assert sum_to_n(5) == 15

# Test case with sum_to_n(10)
assert sum_to_n(10) == 55

# Test case with sum_to_n(1)
assert sum_to_n(1) == 1
```

These tests confirm that the `sum_to_n` function behaves as expected, providing consistent results for a variety of input values of `n`.  This makes the function a reliable tool for calculating the sum of the first `n` positive integers.