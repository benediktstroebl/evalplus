```python
def filter_integers(values):
    """
    Filter given list of any python values only for integers.

    Args:
        values (List[Any]): List of possible values.

    Returns: a list of integers (List[int]).)
    """
    # Create an empty list to store integers
    integer_list = []
    # Loop through all elements in the input list
    for value in values:
        # If the element is an integer, append it to the list
        if isinstance(value, int):
            integer_list.append(value)
    # If the element is not an integer, skip it
        else:
            pass
    return integer_list
```