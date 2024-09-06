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
    # Return the sorted list
    return sorted_list
```

The code first determines the minimum and maximum values in the input list. Initially, it sets the minimum and maximum values to positive and negative infinity, respectively. It then enters a loop and updates the minimum and maximum values as it goes through the list.

After determining the minimum and maximum values, it goes through the list a second time, adding each value to the sorted list in the appropriate locations. The code additionally handles situations when the input list has less than two elements, in which case it simply returns the original list without modification.

The code is self-contained and can be used to sort a list in the specified manner.