```python
def sort_even(lst):
    """This function sorts a list so that all the odd indices are in their correct positions, while keeping the even indices in their original order.
    
    Args:
        lst (list): The list to be sorted
    
    Returns:
        list: The sorted list
    """
    return lst[:2] + [item for item in lst[2:]] + lst[-2:]
```