```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squared integers rounded up to the next integer.
    """
    result = 0
    for n in lst:
        result += n**2
    
    return int(result)
```

The function `sum_squares` defines a list of numbers as input and returns the sum of squared integers from the list. It also rounds the sum up to the next integer. The function solves the problem using a for loop that adds each number in the input list and returns the square of each number to the `result` variable. Finally, it returns the `result` rounded up to the next integer.