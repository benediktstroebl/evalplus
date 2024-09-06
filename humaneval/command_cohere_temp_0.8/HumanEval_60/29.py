```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```
This code defines a Python function called `sum_to_n`. This function takes a single argument, `n`, which is an integer. The purpose of this function is to calculate and return the sum of all integers from 1 to `n` (inclusive) using the `sum` function and generating values using the `range` function. The `sum` function takes a sequence of numbers and adds up all its elements, and the `range` function creates a sequence of numbers starting from `start` (inclusive) and ending at `stop` (exclusive), incrementing by `step` if provided.

Here is an example of how to use this function:
```python
print(sum_to_n(10))  # Output: 55
```

This would print the result of 55, which is the sum of the integers from 1 to 10.