```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument `n`, which is an integer. Inside the function, it uses the `sum` function in combination with the `range` function to calculate the sum of all integers from 1 to `n` (inclusive). The `range` function generates a sequence of numbers starting from 1 up to `n`, and the `sum` function adds up all the values in this sequence, providing the total sum. The function returns this sum as its output. 

The docstring explains that the function calculates the sum of integers from 1 to 'n', and provides some test cases as examples that demonstrate how the function behaves for different values of 'n'.