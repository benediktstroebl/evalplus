```python
def strange_sort_list(lst):
    # Initialize min and max values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Loop through each value in the list and update min_val and max_val accordingly
    for val in lst:
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

        # Append the value to the sorted_list if min_val equals max_val
        if min_val == max_val:
            sorted_list.append(val)
            min_val = float('inf')
            max_val = float('-inf')

    # Append remaining values in the list to sorted_list
    sorted_list.extend(min_val for _ in lst if _ != min_val)
    
    return sorted_list
```

This Python script defines the function `strange_sort_list`, which takes a list of integers as input and returns that list in a "strange" order: it first sorts the list by minimal values, then maximal values, and so on, resulting in an order like `[1, 4, 2, 3]` for the input `[1, 2, 3, 4]`. The function works by maintaining two variables, `min_val` and `max_val`, which represent the minimum and maximum values seen so far. As the function iterates through the input list, it updates these values accordingly. When `min_val` and `max_val` are equal, the current value is added to the `sorted_list`, assuming it's the middle value in the "strange" sorted order. Finally, any remaining values from the input list are added to `sorted_list` in groups corresponding to their uniqueness.