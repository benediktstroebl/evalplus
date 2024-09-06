```python
def sum_to_n(n):
    """Returns the sum of the first n numbers (1 through n)."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument `n`, representing a target number. The function leverages the `range` function to generate a sequence of numbers from 1 to `n`, and then uses the `sum` function to add up all the numbers in this sequence, providing the total sum of the first `n` numbers. 

The function includes a docstring that provides a concise description of its purpose and behavior, giving clarity to anyone who may later be reading or using this code. 

To test this function, you can add the following code to verify its behavior:
```python
# Testing the sum_to_n function
# Checking a specific case
assert sum_to_n(30) == 465

# Checking the boundary case
assert sum_to_n(1) == 1

# Checking for correctness with a large value
assert sum_to_n(100) == 5050

# Checking for correctness with a small value
assert sum_to_n(5) == 15

# Checking for correctness with a medium value
assert sum_to_n(10) == 55
```

This test suite includes a variety of test cases that cover a specific example, boundary cases, and a range of values to ensure that the function behaves as expected across different scenarios.