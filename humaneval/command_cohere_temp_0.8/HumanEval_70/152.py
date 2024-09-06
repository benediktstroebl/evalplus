```python
def strange_sort_list(lst):
    # Initialize min and max values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Traverse through the list to find the min and max values
    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    # Add the min and max values to the sorted list
    sorted_list.extend([min_val, max_val])

    # Set the min and max values to the remaining values in the list
    # and repeat the process until the list is empty
    while lst:
        min_val = max(lst)
        max_val = min(x for x in lst if x > min_val)
        sorted_list.extend([min_val, max_val])
        lst = [x for x in lst if x != min_val and x != max_val]

    return sorted_list
```

The code initially identifies the minimum and maximum values in the list, which are then added to the `sorted_list`. This process is repeated until the original list is empty, ensuring that the remaining elements are in the correct order. The approach is efficient and satisfies the problem requirements, but it is essential to note that it has a worst-case time complexity of O(n^2), where n is the number of elements in the input list.