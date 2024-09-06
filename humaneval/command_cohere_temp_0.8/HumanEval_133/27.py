```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): List of numbers.
        
    Returns:
        int: Sum of squared integers rounded up to the next integer.
    """
    result = sum(int(round(n)**2 for n in lst if n != 0 and isinstance(n, (int, float))))
    return result
```

The function `sum_squares` takes a list of numbers as an argument and returns the sum of the squares of the integers in the list, rounded up to the next integer. It does this by using a generator expression within the `sum` function, which iterates over the list, squares each element that is not zero or a non-integer float, and rounds it up to the next integer using the `int` function. The resulting sum is then returned as an integer. 

This Python script solves the problem while maintaining code flexibility and readability, as it is self-contained and can be easily reused and integrated into larger projects.