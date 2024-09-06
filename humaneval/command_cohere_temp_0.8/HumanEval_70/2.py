```python
def strange_sort_list(lst):
    # Determine the minimum and maximum values in the list
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the output list with the initial minimum value
    sorted_list = [min_val]
    
    # Iterate through the original list
    for val in lst:
        # If the current value is smaller than the maximum found so far
        if val < max_val:
            # Add the current value to the output list
            sorted_list.append(val)
        else:
            # Replace the maximum value in the output list with the current value
            sorted_list.append(max_val)
            # Update the maximum value to the current value
            max_val = val
    
    # Add remaining maximum value to the output list
    sorted_list.append(max_val)
    
    return sorted_list
```

This function takes in a list of integers, and follows the strange sorting algorithm as described in the problem statement. It initializes the resulting sorted list with the smallest value in the input list, and then iterates through the original list.

It compares each element to the maximum value seen so far, if it's smaller, it gets appended to the result, if it's larger, it replaces the maximum value in the result and updates the maximum. After the loop, the last remaining maximum is appended to the result. This process creates the desired 'strange' sort order.

The function returns the list in this strange ordered structure, where we start with the minimum value, then the maximum, then the second minimum, and so on.