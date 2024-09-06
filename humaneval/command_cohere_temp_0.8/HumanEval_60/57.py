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
This Python script defines a function `sum_to_n` that calculates the sum of numbers between 1 and `n` (`inclusive`). It uses the `sum` function with the `range` function as its argument to generate a series of numbers from 1 to `n` and then adds them up. 

The function features an argument called `n`, which is used to define the number of integers to be summed, and it returns an integer value. 

To test this function, you can call it with different values for `n` to verify its behavior:
```python
# Test Case 1
n = 30
expected_sum = 465
sum_result = sum_to_n(n)
assert sum_result == expected_sum

# Test Case 2
n = 100
expected_sum = 5050
sum_result = sum_to_n(n)
assert sum_result == expected_sum

# Test Case 3
n = 5
expected_sum = 15
sum_result = sum_to_n(n)
assert sum_result == expected_sum

# Test Case 4
n = 10
expected_sum = 55
sum_result = sum_to_n(n)
assert sum_result == expected_sum
```
Each test case ensures that the function `sum_to_n` produces the anticipated sum for a specific value of `n`.  This series of tests will confirm that the function works correctly for a variety of scenarios.  The function is then annotated with docstrings to provide more information about it.