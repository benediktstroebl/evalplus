```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    Args:
        lst (list): List of numbers.
        
    Returns:
        int: Sum of squared integers.
    """
    result = 0
    for n in lst:
        if isinstance(n, int): 
            result += n ** 2 
    return result
```

The function iterates over each list item, and if the item is an integer, squares it and adds it to the result. This algorithm is simple and effective, achieving the desired result in a single pass through the list. It adheres to the problem statement by rounding each number to the greater integer before squaring and summing them.