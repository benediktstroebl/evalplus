```python
def max_element(l: list):
    """Return maximum element in the list.
    
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if not l:
        raise ValueError("Input list is empty")
    
    max_element = max(l)
    return max_element
```

The code defines a function `max_element` that takes a list `l` as input and returns the maximum element in the list. The function initially checks if the list is empty; if so, it raises a ValueError with the message "Input list is empty." To determine the maximum element, the function employs the built-in `max` function to evaluate the maximum value in the list. 

The script effectively handles a variety of input lists, including both positive and negative integers, and returns the highest element present in the list.