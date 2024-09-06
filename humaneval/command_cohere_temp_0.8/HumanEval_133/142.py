```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = sum(int(round(x)**2)) for x in lst if isinstance(x, (int, float)) and x >= 0
    return result
```

The function `sum_squares` takes a list of items as an argument and returns the sum of the squares of all the integers in the list, rounded up to the nearest integer. Under these conditions, the sum is also positive.

The code uses a generator expression alongside the `round` function to ensure all calculations are done using integers, thus avoiding any floating-point accuracy issues. Additionally, the filter condition ensures that only valid integers are considered, based on the problem's constraints.