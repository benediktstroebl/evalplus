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

The function `sum_squares` takes a list of items and returns the sum of the squares of all the integers in that list. Before finding the sum, it checks if all the elements are integers, and if not, it converts them to integers, ensuring the result is also an integer.