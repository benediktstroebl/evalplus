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
        if num < 0:
            num = int(num * 10 / 10.0)
        else:
            num = int(num + 1e-5)
        result += num ** 2

    return result
```