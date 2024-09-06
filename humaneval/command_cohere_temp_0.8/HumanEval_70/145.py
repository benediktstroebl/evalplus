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
            min_val = min(min_val, val)
            max_val = max(max_val, val)
    
    # Append the last maximum value
    sorted_list.append(max_val)
    
    return sorted_list
```

The function `strange_sort_list` takes in a list of integers and returns that list in a "strange" order, which starts with the smallest value, then the largest value among the remaining integers, then the smallest value again, and so on. The function initializes the sorted list with the smallest value, then iterates through the original list, comparing each value to the current smallest and largest values. The result is a sorted list in the desired "strange" order, which follows the definition provided in the prompt.