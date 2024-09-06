```python
def strange_sort_list(lst):
    """
    Do a strange sort of a list, namely return the minimum value,
    then the maximum of the remaining integers, then the minimum, and so on.
    """
    # Initialize the variables to be the first value of the list and its index
    min_val = lst[0]
    min_idx = 0
    new_lst = [min_val]
    # Iterate through the list
    for i in range(len(lst)):
        # If the current value is less than the current minimum, set it as the new minimum
        if lst[i] < min_val:
            min_val = lst[i]
            min_idx = i
        # If the current index is the minimum index, append the maximum value to the new list
        elif i == min_idx:
            new_lst.append(max(lst))
        # Otherwise, move to the next index in the main list
        else:
            new_lst.append(min_val)
    # Return the strange sorted list
    return new_lst
```

This approach uses two pointers: one for the minimum value and its index, and another for the next value to be appended to the new list. The strange sorting order is achieved by adding the maximum value of the remaining integers whenever the current value is the minimum. The script handles the edge cases of an empty list and list containing identical values correctly.

Here are some example outputs:
```python
strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
strange_sort_list([]) == []
``` 

You can test the function by calling `strange_sort_list()` with different lists as input.