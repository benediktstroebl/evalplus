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

        # Append the current minimum or maximum value to the sorted list
        sorted_list.append(min_val if val == max_val else max_val)

    return sorted_list
```

The function `strange_sort_list` initially identifies the minimum and maximum values in the list. Subsequently, it constructs an array where alternating entries are the minimum and maximum values encountered. This approach yields the desired "strange" sorting order, where the smallest value represents the first element, followed by the largest value among the remaining entries, and so forth. 

This approach guarantees that the sorted list adheres to the specified odd sorting pattern, as exemplified in the problem statement.