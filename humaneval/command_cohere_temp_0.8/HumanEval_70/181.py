```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    
    # Initialize the sorted list
    sorted_lst = [min_]
    
    # Loop through the original list
    for num in lst:
        if num == min_:
            sorted_lst.append(max(lst))
        elif num == max_:
            sorted_lst.append(min(lst))
        else:
            sorted_lst.append(num)
    
    return sorted_lst
```

This function takes a list as input and returns a list sorted in the specified strange order. It first finds the minimum and maximum values in the list with the `min()` and `max()` functions. It then initializes a new sorted list with the minimum value found. It then iterates through the original list, appending the maximum value in the list at each iteration if the current value is the minimum, or the minimum value if the current value is the maximum. If neither of these conditions are met, it appends the current value. This process effectively creates a list sorted in the specified strange order.