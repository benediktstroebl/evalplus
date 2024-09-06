```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions with maximum value and even positions with minimum value.
    for num in lst:
        if len(sorted_list) % 2 == 0:
            # If the list is even in length, add minimum value
            if num < min_val:
                min_val = num
        else:
            # If the list length is odd, add maximum value
            if num > max_val:
                max_val = num
        sorted_list.append(num)

    return sorted_list
```
The code handles the sorting as per the problem statement, it checks if the length of the `sorted_list` is even or odd to determine whether the current number in the list being sorted is compared to the maximum or minimum value of the remaining numbers to be sorted. As such, it effectively creates the "strange" sort order as described in the problem statement.