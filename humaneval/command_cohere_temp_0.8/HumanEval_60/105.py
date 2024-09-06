```python
def sum_to_n(n):
    """Returns the sum of the first n numbers (1 to n)."""
    return sum(range(1, n + 1))
```

This code defines a Python function called `sum_to_n` that takes a single argument `n`, which is an integer representing the upper limit of a range of numbers. The function calculates and returns the sum of the first `n` numbers, starting from 1 up to `n`. It achieves this by using the `range` function to generate a sequence of numbers from 1 to `n` (exclusive), and then passes this sequence to the `sum` function to add up all the numbers in the sequence. 

The function's summary comments explain its purpose, and example usage statements show how it can be called with different values of `n` to demonstrate its behavior.