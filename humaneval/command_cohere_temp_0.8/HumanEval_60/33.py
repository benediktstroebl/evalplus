```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum

    Returns:
        int: Sum of the first n integers
    """
    return sum(range(1, n + 1))
```

This code defines a function called `sum_to_n` that takes an integer argument `n`. It returns the sum of the first `n` integers from 1 to `n`. To do this, it uses Python's `range` function to generate a sequence of numbers from 1 to `n` and passes this sequence to the `sum` function to calculate the sum. 

This solution complies with the problem statement and the given tests. You can use it as a standalone function as seen in the comments. 
If you'd like, we can go through and break down the problem and how this solution tackles it.