```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the sorted list
    sorted_list = [min_val]
    
    # Iterate through the original list
    for val in lst:
        if val == min_val:
            # If the current value is the minimum, add it to the sorted list
            sorted_list.append(val)
        elif val == max_val:
            # If the current value is the maximum, replace the minimum value in the sorted list
            sorted_list.append(val)
            min_val = max_val
        else:
            # Otherwise, update the maximum value
            max_val = val
    
    # Add remaining elements in the original list to the sorted list
    sorted_list.extend(lst)
    
    return sorted_list
```

The code follows the strange sorting algorithm as described in the problem statement. It simultaneously maintains the minimum and maximum values encountered in the original list `lst`, and iteratively updates the `sorted_list` by adding either the minimum or maximum value, whichever is encountered. The resulting sorted list is then returned.