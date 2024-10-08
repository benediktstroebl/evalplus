```python
def strange_sort_list(lst):
    # Helper function to find the max element from the remaining list
    def max_remaining(L):
        max_so_far = float('-inf')
        for num in L:
            if num > max_so_far:
                max_so_far = num
        return max_so_far

    # Special case when the input list is empty
    if not lst:
        return []

    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)

    # Initialize the output list with the minimum value
    sorted_list = [min_val]

    # Iterate over the remaining elements in the list
    for num in lst:
        # If the current element is the maximum of the remaining elements, add it to the output list
        if num == max_remaining(lst[:len(sorted_list)]):
            sorted_list.append(max_val)
            lst.remove(max_val)
            max_val = max_remaining(lst)

        # Otherwise, add the minimum value to the output list
        else:
            sorted_list.append(min_val)
            min_val = min(lst)

    # Append the remaining maximum value to the output list
    if max_val != min_val:
        sorted_list.append(max_val)

    return sorted_list
```

This Python script implements the `strange_sort_list` function, which sorts a given list of integers in a strange order as per the problem statement. It starts with the minimum value and then places the maximum value of the remaining list, alternating between the minimum and maximum values until the list is sorted. The script includes a `max_remaining` helper function to find the maximum value from the remaining list, and it handles cases where the input list is empty or contains only one value. The resulting sorted list is returned.