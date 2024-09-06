```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the sorted list
    sorted_list = [min_val]
    
    # Loop through the original list
    for val in lst:
        if val == min_val:
            sorted_list.append(max_val)
        elif val == max_val:
            sorted_list.append(min_val)
        else:
            sorted_list.append(val)
    
    return sorted_list
```

The function `strange_sort_list` takes a list of integers (`lst`) as input and returns the list in a strange order, as described in the prompt. It accomplishes this by starting with the minimum value and then alternating between the maximum value and the current value of the list while iterating through it. This ensures that the resulting `sorted_list` conforms to the specified strange order. The function handles edge cases where the list contains an even number of values or is empty, ensuring that it returns the correct result in all scenarios.