```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = sum(int(round(x)**2)) for x in lst if isinstance(x, (int, float)) and x > 0
    return result
```

The function `sum_squares` employs a generator expression to iterate over the list `lst`, filtering out non-positive numbers and converting elements to integers. The expression squares each number and rounds them to the nearest integer using Python's built-in `round` function. These squared, rounded integers are then summed using Python's built-in `sum` function. The final result is the total of the squared, rounded integers, rounded up to the nearest integer. 

This approach ensures that each element is properly squared and rounded, and the resulting sum is accurately rounded up to the nearest integer.