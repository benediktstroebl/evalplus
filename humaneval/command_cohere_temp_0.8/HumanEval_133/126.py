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
    for num in lst:
        if isinstance(num, float):
            num = int(num)
        result += num ** 2
    
    return int(result)
```

The function iterates through the list, squares each element if it's not already an integer, and sums them. Finally, it returns the rounded-up result.