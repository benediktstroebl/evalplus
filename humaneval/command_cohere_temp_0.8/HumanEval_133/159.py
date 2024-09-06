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
        rounded_n = int(n)
        result += rounded_n ** 2
    return result
```

The function `sum_squares` takes a list of numbers, squares each integer in the list, and returns their sum. It assumes that the list contains only integer values or values that can be converted to integers. If a value in the list cannot be converted to an integer, it will be ignored in the calculation.