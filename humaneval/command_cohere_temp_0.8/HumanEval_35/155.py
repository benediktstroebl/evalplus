```python
def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list of elements.

    Returns:
        int or float: The maximum element in the list.
    """
    if not l:
        return None  # Return None for an empty list
    max_el = l[0]
    for num in l:
        if num > max_el:
            max_el = num
    return max_el
```

The max_element function takes a list `l` as input and iterates through the list, comparing each element to the current maximum value stored in the max_el variable. The element that exceeds the current maximum is assigned to max_el, ensuring that the maximum element is tracked and returned at the end of the function. This approach is efficient and can handle both positive and negative numbers gracefully.