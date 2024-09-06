```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. Inside the function, it uses the `sum` function to calculate the sum of integers from 1 to `n` (inclusive) and returns the result. The `range` function is used to generate a sequence of numbers from 1 to `n` (again, inclusive), and this sequence is passed to the `sum` function to compute the sum. The result is then returned as the output of the `sum_to_n` function. 

The function includes a docstring (`"""`) that provides a brief description of its purpose, which is to return the sum of integers from 1 to `n`. This docstring is useful for providing information about what the function does and how it's used. 

This code is self-contained, meaning it can be copied and pasted into a Python environment without relying on external variables or functions.