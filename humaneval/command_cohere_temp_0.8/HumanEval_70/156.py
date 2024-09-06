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
    
    # Add the remaining values of the original list to the sorted list
    sorted_list.extend(lst[len(sorted_list):])
    
    return sorted_list
```

This Python script defines a function called `strange_sort_list` that takes in a list of integers (`lst`) as input. It sorts the list using a strange ordering algorithm, as described in the problem statement. Here's how it works:
1. The function first identifies the minimum and maximum values in the input list: `min_val = min(lst)` and `max_val = max(lst)`
2. It initializes an empty list called `sorted_list` to store the sorted elements, starting with the minimum value: `sorted_list = [min_val]`
3. The function iterates through the original list, using two pointers:
   - `min_val` always points to the minimum value in the current window of interest (either the entire list or half of it).
   - `max_val` always points to the maximum value in the current window of interest.
4. For each value `val` in the original list:
   - If `val` is equal to `min_val`, it belongs in the current window of the `sorted_list`, so it is appended: `sorted_list.append(val)`
   - If `val` is equal to `max_val`, it also belongs in the current window of the `sorted_list`, so it is appended: `sorted_list.append(val)`
   - Otherwise, the function updates `min_val` and `max_val` to narrow down the window to either the first half or the second half of the remaining values (including `val`).
5. After processing all values of the original list, the function adds the remaining values (the second half) to the `sorted_list`: `sorted_list.extend(lst[len(sorted_list):])`

Finally, the function returns the `sorted_list`, which represents the input list sorted in the strange order as described in the problem statement.