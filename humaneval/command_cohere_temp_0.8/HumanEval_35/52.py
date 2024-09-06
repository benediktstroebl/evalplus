```python
def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list of elements.

    Returns:
        int or float: The maximum element in the list.
    """
    # initialize max element
    max_el = float('-inf')

    # iterate through the list and update max_element if a greater element is found
    for x in l:
        if x > max_el:
            max_el = x

    return max_el
```

This function uses the `float('-inf')` value to initialize `max_element` to the lowest possible value, which ensures that any element in the list will be greater than the initial value and therefore can be assigned the maximum value as the script runs. The function loops through the list, comparing each element to the current `max_element`, and updates it if it finds a greater element. As a result, the max_element will be returned at the end of the function.