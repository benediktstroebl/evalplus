Here's the self-contained Python function that filters and returns integers from a given list:
```python
def filter_integers(values):
    """ Filter given list for integers
    :param values: List of any python object
    :return: List of int
    """
    return [x for x in values if isinstance(x, int)]
```

This function takes a list of values as input and returns a new list that contains only the integers from the original list. The function uses a simple filtering logic to identify and return only the integer elements from the input list. 

Additionally, I've included some comments to provide clarity on the code's functionality and purpose.