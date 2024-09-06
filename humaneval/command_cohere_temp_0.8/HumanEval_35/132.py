```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
    - l (list): List of elements
    
    Returns:
    - int or float: Maximum element in the list
    
    Example:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # check if the list is empty
    if not l:
        return None
    # initialization
    max_so_far = l[0]
    for x in l:
        # update max_so_far if a number is greater than the current max
        if x > max_so_far:
            max_so_far = x
    return max_so_far
```

The function iterates through the list and keeps track of a maximum element so far (`max_so_far`). Whenever a number greater than `max_so_far` is encountered, the `max_so_far` is updated, ensuring that the maximum value is tracked and returned at the end. This algorithm is known as the "Iterative Monotone Maximum" approach, mainly focused on finding the maximum element in a non-empty list.  It is efficient and has a time complexity of O(n), where n is the number of elements in the input list.