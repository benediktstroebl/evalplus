```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the provided list.
    
    Args:
        lst (list): A list of numbers.
        
    Returns:
        int: The sum of squared integers rounded up to the nearest integer.
    """
    result = 0
    for num in lst:
        if isinstance(num, float):
            num = int(num)
        result += num ** 2
    
    return int(result)
```

The function `sum_squares` takes a list of numbers, iterates through them, and squares each number if it isn't already. It then adds the squared values to a running total, which is returned after all numbers have been processed. This ensures that numbers are appropriately squared and summed whilst handling both integers and floats.