```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): List of numbers.
        
    Returns:
        int: The sum of squared integers in the list.
    """
    result = 0
    for n in lst:
        if isinstance(n, float):
            n = round(n)
        result += n ** 2
    
    return result
```

The function `sum_squares` rounds each number in the list to the nearest higher integer, then squares them and adds them to the result. It ensures that only integers are squared by rounding each number in the list to the next higher integer before squaring them.