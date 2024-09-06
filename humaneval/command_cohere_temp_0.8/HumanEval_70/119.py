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
        else:
            continue

        # Append the current minimum or maximum value to the sorted list
        sorted_list.append(min_val if len(sorted_list) == 0 or sorted_list[-1] == min_val else max_val)

    return sorted_list
```

The code exploits the fact that the list is sorted alternately according to the minimum and maximum values of the remaining integers. Hence, we start by finding the minimum and maximum values of the list, initialized with positive and negative infinite values respectively. In the loop, we check if the current value is smaller than the minimum or greater than the maximum, in which case we update the respective variable. If the current value is neither the smallest nor the largest, it is skipped. When updating the sorted list, we use the maximum value if the previous value in the sorted list is the minimum, and vice versa, ensuring the correct alternating sorting pattern.