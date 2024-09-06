```python
def strange_sort_list(lst):
    # Initialize min and max values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd places with min value and even places with max value
    for val in lst:
        if len(sorted_list) % 2 == 0:
            if val < max_val:
                sorted_list.append(val)
                max_val = val
        else:
            if val > min_val:
                sorted_list.append(val)
                min_val = val

    return sorted_list
```

This Python script defines a function called `strange_sort_list` that takes a list of integers as input. It sorts the list in a "strange" order: it starts with the minimum value, then places the maximum value among the remaining integers, then the minimum value again, and so on. The function iterates through the input list, maintaining track of the minimum and maximum values encountered. It alternates between placing the current value in the sorted list if it is either greater than the current minimum or less than the current maximum, effectively achieving the desired "strange" sorting. The script ensures that empty input lists return an empty list as well.