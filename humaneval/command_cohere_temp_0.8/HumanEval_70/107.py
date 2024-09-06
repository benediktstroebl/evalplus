```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with maximum value and even positions with minimum value.
    for i in lst:
        if i > max_val:
            max_val = i
            odd = True
        elif i < min_val:
            min_val = i
            odd = False
        elif odd is True:
            sorted_list.append(max_val)
            odd = False
        else:
            sorted_list.append(min_val)
        odd = not odd

    # Add the remaining maximum and minimum values to the end of the list.
    sorted_list.append(max_val)
    sorted_list.append(min_val)

    return sorted_list
```

The function works by initially storing the minimum and maximum values at the beginning and end of the list respectively. It then alternates between appending the maximum value and the minimum value to the growing list, ensuring that odd positions contain the maximum value and even positions contain the minimum value. Finally, the remaining maximum and minimum values are added to the end of the list and returned.

The approach takes advantage of the fact that the sorting algorithm is asked to perform odd and even positions sorting alternatively. Thus, we can construct the desired 'strange' sorted list by picking maxima for odd positions and minima for even positions.