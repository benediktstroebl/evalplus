```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Ensure that the list has at least one element
    if lst:
        # Find the minimum value
        min_val = min(lst)

        # Find the maximum value among the remaining list values
        max_val = max(val for val in lst if val != min_val)

        # Append the two values to the sorted list
        sorted_list.extend([min_val, max_val])

        # Recursively sort the remaining elements
        sorted_list.extend(strange_sort_list(lst[2:]))

    # Return the sorted list in the specified order
    return sorted_list
```

This Python script solves the problem with a clear and efficient algorithm using recursion, ensuring the list is sorted in the specified 'strange' order.