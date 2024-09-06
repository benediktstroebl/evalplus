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

        # Append the current value to the sorted list
        sorted_list.append(val)

    # If the list has fewer than two elements, return the original list
    if len(lst) < 2:
        return lst
    # Return the sorted list, otherwise
    return sorted_list
```

The function `strange_sort_list` takes a list of integers as input and attempts to sort it using the strange sorting algorithm described in the problem statement. It initializes min_val and max_val to positive and negative infinity, respectively, and the sorted list as an empty list.

It then iterates over the original list, updating min_val and max_val as it encounters lower and higher values, respectively. When it finds a value equal to min_val or max_val, it appends the value to the sorted list.

Finally, the function checks if the length of the original list is less than 2. If so, it returns the original list, assuming that the strange sort algorithm is not applicable to lists with fewer than two elements. Otherwise, it returns the sorted list.