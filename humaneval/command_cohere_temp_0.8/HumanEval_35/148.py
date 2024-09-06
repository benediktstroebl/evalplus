```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
    - l (list): List of elements
    
    Returns:
    - int or float: Maximum element in the list
    """
    if not l:
        raise ValueError("List cannot be empty")
    
    max_element = max(l)
    return max_element
```

This script defines a function 'max_element' that takes a list of elements as an argument and returns the maximum element in the list. It first checks if the input list is empty, and if so, raises a 'ValueError' with the message "List cannot be empty". If the list is not empty, it simply identifies the maximum element using the 'max' function and returns it.