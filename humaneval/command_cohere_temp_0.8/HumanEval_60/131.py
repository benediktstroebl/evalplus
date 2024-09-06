```python
def sum_to_n(n):
    """Returns the sum of integers from 1 to n."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument, `n`, which is an integer representing the upper limit of a range of numbers. The function uses the `sum` function to calculate the sum of integers in the range from 1 to `n` (inclusive). The `range` function generates a sequence of numbers from 1 to `n`, and the `sum` function adds up all the values in this sequence, providing the total sum. 

The function then returns this total sum as its output. The function has a docstring (`''"`...) that provides documentation for the function, including a simple test of the function's behavior with example outputs for various values of `n`.

If you are testing this function, you can use the `assert` statement to check that the output is as expected: 
 ```python
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
``` 
This will help you ensure that the function behaves as expected.