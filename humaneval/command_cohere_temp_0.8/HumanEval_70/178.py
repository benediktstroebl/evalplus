```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    
    # Initialize the sorted list
    sorted_lst = [min_]
    
    # Loop through the original list
    for val in lst:
        if val == min_:
            sorted_lst.append(max(lst))
        elif val == max_:
            sorted_lst.append(min(lst))
        else:
            sorted_lst.append(val)
    
    return sorted_lst
```

The function `strange_sort_list` takes a list of integers as input and attempts to sort it using the "strange" sorting order described in the problem. It starts by finding the minimum and maximum values in the list, then adds the minimum value first to the sorted list. It then encounters each value in the list, adding the maximum value remaining on the list after each minimum value and vice versa. The loop continues until all values in the original list have been processed. As a result, it returns the list in the desired strange order.