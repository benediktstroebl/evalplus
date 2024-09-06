```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): List of numbers.
        
    Returns:
        int: Sum of squared integers rounded up to the next integer.
    """
    result = sum(int(round(n)**2 for n in lst if n >= 0))
    return result
```

The function `sum_squares` takes a list of numbers as an argument and returns the sum of the squares of the integers in the list, rounded up to the next integer. To achieve this, it iterates through each element in the list using a generator expression. It squares each element and rounds it to the nearest integer using the `round()` function. Only positive integers are considered, as per the problem statement requirements. The sum of the squared integers is then calculated using the `sum()` function, and the result is returned as an integer.