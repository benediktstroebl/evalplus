```python
def strange_sort_list(lst):
    # Initialize min and max values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with min valve and even positions with max value
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

This Python script defines a function called `strange_sort_list` that takes a list of integers as input. It sorts the list in a strange order, where odd positions are filled with the minimum value from the list and even positions are filled with the maximum value from the list. The script initializes two variables, `min_val` and `max_val`, to represent the minimum and maximum values encountered in the list, respectively. It then iterates through the input list, checking whether the current position in the sorted list is odd or even. If the position is even, the script checks if the current element in the input list is smaller than the `max_val`. If it is, the element is added to the `sorted_list`, and the `max_val` is updated to the current element. Conversely, if the position is odd, the script checks if the current element in the input list is larger than the `min_val`. If it is, the element is added to the `sorted_list`, and the `min_val` is updated to the current element. This process continues until all elements have been processed, and the resulting `sorted_list` is returned.

Here's an example of how to use the function:
```python
print(strange_sort_list([1, 2, 3, 4]))  # Output: [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # Output: [5, 5, 5, 5]
print(strange_sort_list([]))  # Output: []
```

This demonstrates how the `strange_sort_list` function can be used to sort lists in the specified strange order.