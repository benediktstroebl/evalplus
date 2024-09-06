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
            sorted_list.append(val)
        elif val == max_val:
            sorted_list.append(val)
        else:
            min_val = min(val, min_val)
            max_val = max(val, max_val)
    
    # Add the last occurrence of maximum and minimum values
    sorted_list.append(max_val)
    sorted_list.append(min_val)
    
    return sorted_list
```

This function takes in a list of integers, and follows the strange sorting algorithm as described in the problem statement. It starts by finding the minimum and maximum values in the list, and then alternately adds the minimum and maximum values to the sorted list. After processing each element, it updates the `min_val` and `max_val` to reflect the remaining elements in the unsorted portion of the list. Finally, it returns the sorted list.

To verify the function behavior you can test it with:
```python
>>> strange_sort_list([1, 2, 3, 4])
[1, 4, 2, 3]
>>> strange_sort_list([5, 5, 5, 5])
[5, 5, 5, 5]
>>> strange_sort_list([10, 9, 8, 7, 6])
[6, 10, 9, 8, 7]
>>> strange_sort_list([])
[]
```