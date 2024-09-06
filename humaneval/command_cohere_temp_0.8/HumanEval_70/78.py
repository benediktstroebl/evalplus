```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the original list
    for val in lst:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val

        # Append the current minimum or maximum value to the sorted list
        if len(sorted_list) == 0:
            sorted_list.append(min_val)
        elif len(sorted_list) == 1:
            sorted_list.append(max_val)

    # If the original list is empty, return an empty list
    if not lst:
        return sorted_list
    # Continue sorting by applying the same logic to the remaining elements
    else:
        mid = len(sorted_list) // 2
        sorted_list[mid], sorted_list[-1] = sorted_list[-1], sorted_list[mid]
        return sorted_list
```

This Python script defines a function called `strange_sort_list` that takes in a list of integers (`lst`) as input. It sorts the list in a "strange" order, where it first identifies the minimum and maximum values in the list, alternates between placing the minimum and maximum values in the sorted list, and maintains this pattern throughout. The script includes a note about edge cases where the behavior is specified. The function returns the sorted list in this specified order.