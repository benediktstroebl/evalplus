```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = float('inf')
    max_val = float('-inf')
    sorted_list = []

    # Iterate through the list and sort odd positions using maximum and even positions using minimum
    for i, num in enumerate(lst):
        if i % 2 == 0:
            # If the current number is greater than the minimum, update min_val and add the number to the result list
            if num >= min_val:
                min_val = num
                sorted_list.append(num)
        else:
            # If the current number is less than the maximum, update max_val and add the number to the result list
            if num <= max_val:
                max_val = num
                sorted_list.append(num)

    return sorted_list
```

The code provides an implementation of the strange sort algorithm, which aims to sort a list of numbers odd positions with the maximum value and even positions with the minimum value. It uses the `enumerate()` function to iterate through the list, saving the index of each element (`i`) as it is processed. Within the loop, it compares the current number (`num`) to the current minimum and maximum values. If the number is greater than or equal to the current minimum, it updates the `min_val` and adds the number to the `sorted_list`. If the number is less than or equal to the current maximum, it updates the `max_val` and adds the number to the `sorted_list`. This process continues until all numbers have been processed. The function returns the `sorted_list` in the specified strange order.