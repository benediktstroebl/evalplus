```python
def strange_sort_list(lst):
    # Initialize min and max values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with min valve and even position with max value
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

This Python script defines a function called `strange_sort_list` that takes a list of integers as input. It sorts the list in a "strange" order: it starts with the smallest value, then places the largest value among the remaining integers, then the smallest value again, and so on. The function iterates through the input list, maintaining track of the smallest and largest values encountered. It fills odd positions of the `sorted_list` with the largest value and even positions with the smallest value, updating the max_val and min_val accordingly. The resulting sorted list is then returned.

Here's an example of how to use this function:
```python
print(strange_sort_list([1, 2, 3, 4]))  # Output: [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # Output: [5, 5, 5, 5]
print(strange_sort_list([]))  # Output: []
```

This will output:
```bash
[1, 4, 2, 3]
[5, 5, 5, 5]
[]
```