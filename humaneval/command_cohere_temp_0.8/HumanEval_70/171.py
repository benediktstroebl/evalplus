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

        # Append the current maximum value to the sorted list
        sorted_list.append(max_val)

        # Swap maximum and minimum values for the next iteration
        max_val, min_val = min_val, max_val

    # Add the remaining maximum value to the sorted list
    sorted_list.append(max_val)

    return sorted_list
```

This Python script defines a function called `strange_sort_list` that takes in a list of integers as input. It sorts the list in a "strange" order: it starts with the smallest value, then inserts the largest value remaining, then the smallest value again, and so on. The function initializes min_val and max_val to positive and negative infinity, respectively, and creates an empty list called `sorted_list` to store the sorted integers. Then, it verifies if the input list is empty. If empty, it returns an empty list. Otherwise, it iterates through the input list, updating min_val and max_val as it goes. It appends the current max_val to `sorted_list` and swaps max_val and min_val for each element. Finally, it returns the sorted_list containing the sorted integers in the specified order.