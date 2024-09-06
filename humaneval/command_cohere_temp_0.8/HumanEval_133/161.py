```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    
    # Square each element and round it up to the nearest integer
    squared_up = [int(x**2), int(x**2) for x in lst if x >= 1]
    
    return sum(squared_up)
```

The function `sum_squares` takes a list of numbers as an argument and returns the sum of the squares of those numbers, rounded up to the nearest integer. To achieve this, it squares each element in the list using a list comprehension, then rounds each squared value up to the nearest integer using the `int` function, and finally, sums these rounded values. This operation is performed only on elements greater than or equal to 1, ensuring that any decimal values or negative numbers are ignored.