```python
def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers.

    Args:
        lst (list): List of integers.

    Returns:
        list: List sorted in strange order.
    """

    # Check if the list is empty
    if not lst:
        return lst

    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    result = [min_val]

    # Iterate over the remaining elements in the list
    for val in lst:
        if val == max_val:
            result.append(val)
        elif val < max_val:
            result.append(val)
        else:
            result.append(max_val)
            max_val = val

    return result
```

The code checks if the input list is empty and returns it as is if that is the case. Otherwise, it finds the minimum and maximum values from the list and starts constructing the result list by adding the minimum value initially and then alternating between adding the current value and the maximum value of the remaining list until all elements are processed. The maximum value is tracked dynamically by comparing the current value to it.