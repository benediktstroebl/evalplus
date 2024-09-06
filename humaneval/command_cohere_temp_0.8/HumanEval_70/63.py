```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the output list with the minimum value
    sorted_list = [min_val]
    
    # Iterate through the original list
    for val in lst:
        if val == min_val:
            # If the current value is the minimum, add it to the output list
            sorted_list.append(val)
        elif val == max_val:
            # If the current value is the maximum, replace the minimum value in the output list
            sorted_list.append(val)
            min_val = max_val
        else:
            # Otherwise, update the maximum value
            max_val = val
    
    # Add remaining elements in the list
    sorted_list.extend(lst[len(sorted_list):])
    
    return sorted_list
```

This code defines the `strange_sort_list` function, which takes a list of integers (`lst`) as input and returns the list in a strange order as described in the problem statement. It starts by finding the minimum and maximum values in the list and initializing an empty list called `sorted_list` to store the sorted elements. It then enters a loop where it iterates through the original list. If the current value is the minimum, it is added to the `sorted_list`. If it is the maximum, it replaces the minimum value in the `sorted_list`. Otherwise, it updates the maximum value.

After the loop, the function extends the `sorted_list` with any remaining elements from the original list, ensuring that all elements are properly sorted in the strange order as described in the problem statement.