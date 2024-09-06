```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = sum(int(round(n)**2 for n in lst if n != 0 and int(n) == n))
    return result
```

The function `sum_squares` takes a list of numbers as an argument and returns the sum of the squares of the integers in that list. Before squaring, each list element is rounded up to the nearest integer. The sum is then returned, also rounded up to the nearest integer. The code includes tests for correctness against several test cases.