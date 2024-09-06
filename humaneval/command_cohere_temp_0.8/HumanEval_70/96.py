```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the original list
    for val in lst:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val

        # Append the current value to the sorted list
        sorted_list.append(val)

    # If the minimum value hasn't been added, add it to the end
    if min_val != float('inf'):
        sorted_list.append(min_val)

    # If the maximum value hasn't been added, add it to the beginning
    if max_val != float('-inf'):
        sorted_list.insert(0, max_val)

    return sorted_list
```

The function `strange_sort_list` takes a list of integers (`lst`) as input and returns the list in a strange order as described in the prompt. It first finds the minimum and maximum values from the list and stores them in `min_val` and `max_val`, respectively. Then, it constructs a sorted list by appending the values in the order they are encountered, ensuring that the minimum and maximum values are placed correctly. Finally, it checks if the minimum and maximum values were already placed and adds them to the appropriate positions if needed, ensuring the "strange" order of sorting.