```python
def filter_integers(values):
    """
    Filter given list of any python values only for integers.
    Args:
        values (List[Any]): A list of mixed values
    
    Returns:
        List[int]: A list of integers only.
    """
    
    values = [1, 2, 3, 'three', three, [0, 1, 2, 'three', True, []]
    ]
    integers = [x for x in values if type(x) == int]
    return integers
```