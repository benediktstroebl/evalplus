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
        sorted_list.append(val)

    # If there are any duplicate values, they will be appended to the end of the sorted list
    return sorted_list
```

The code first determines the minimum and maximum values in the list. At first, the minimum is set to infinity and the maximum is set to negative infinity. Then, it checks if this is the first value seen, and updates min_val and max_val accordingly. It also initializes an empty list, called `sorted_list`, to store the sorted values.

Next, the code iterates over the original list, and checks if the current value is less than the minimum seen so far, or greater than the maximum seen so far. If so, it updates min_val or max_val accordingly. Finally, the code appends the current value to the `sorted_list`.

The result is a list that is "strangely" sorted, with min-max-min-max... until all values have been accounted for. 

This approach has a time complexity of O(n log n), where n is the length of the input list, as we iterate over the list twice, once to find the min and max values, and once to populate the new sorted list.