```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions using max_val and even positions using min_val
    for val in lst:
        if len(sorted_list) % 2 == 0:
            if val < min_val:
                min_val = val
            elif val > max_val:
                max_val = val
            sorted_list.append(min_val)
        else:
            if val < min_val:
                min_val = val
            elif val > max_val:
                max_val = val
            sorted_list.append(max_val)

    return sorted_list
```

The provided code defines a Python function called `strange_sort_list` that takes a list of integers as input and sorts it into a "strange" order: it first places the smallest element at the start, then the largest remaining element, then the second-smallest, and so on. The result is a list that alternates between the maximum and minimum values in the input list. The code initializes variables `min_val` and `max_val` to positive and negative infinity, respectively, to keep track of the minimum and maximum values encountered. It also creates an empty list `sorted_list` where the sorted elements will be stored. The code then iterates through the input list, checking whether the current position in the list is even or odd to determine whether to use the maximum or minimum value of the current element. If the current element is smaller than `min_val`, it updates `min_val`; if it's larger than `max_val`, it updates `max_val`. The sorted value (either minimum or maximum) is added to the `sorted_list`. Finally, the function returns the `sorted_list` containing the elements sorted in the strange order as specified.