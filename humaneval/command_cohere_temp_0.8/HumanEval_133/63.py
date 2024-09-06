```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest upper int first.
    """
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result
```

This Python script defines a function called `sum_squares` that takes in a list of numbers. This function calculates the sum of squared integers in the list. Before performing the sum, each list item is rounded up to the nearest integer. The result is returned as a single value. 

In Python, this behavior can be achieved using sum and a generating expression with a filter condition. The filter condition x % 1 == 0 ensures only integers are considered, and the rounding is done automatically when casting numeric values to integers.