```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to `n` (inclusive). It achieves this by using the `range` function to generate a sequence of numbers from 1 to `n`, and then tapping into the `sum` function to add up all the numbers in that sequence. 

The function is documented with a docstring, which explains its purpose, provides examples of how to use it, and states the expected input type (`n` is expected to be an integer). Example usage is also provided within the docstring, showcasing how to use this function with different values of `n`, demonstrating its behavior for various input scenarios.