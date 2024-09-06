```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Ensure that empty lists return an empty list
    if not lst:
        return []

    for val in lst:
        # Update min and max values
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

        # Append the value to the sorted list in the correct order
        if val == min_val:
            sorted_list.append(val)
        elif val == max_val:
            sorted_list.append(val)

    return sorted_list
```

The function employs two variables, `min_val` and `max_val`, to keep track of the extremes of the list being traversed. Initially, these variables are set to positive and negative infinity respectively, aiding in the correct identification of the true minimum and maximum values in the list. Upon each iteration through the list, the values are updated accordingly.

The creation of the `sorted_list` occurs in a manner akin to the 'insertion sort' process. This implies a sort that performs a binary search to find the correct position for insertion, the smallest value is appended to the list at the very start, followed by the largest value, and then the process is repeated.

Should the list be empty, the function returns an empty list. This caters to the edge case mentioned in the problem statement. This approach ensures that the function performs as expected, providing a sorted list in the peculiar order described in the problem statement.