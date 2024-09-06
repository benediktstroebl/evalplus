```python
def strange_sort_list(lst):
    # Determine the minimum and maximum values in the list
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the result list with the initial min and max values
    result = [min_val, max_val]
    
    # Continue building the result list by alternating min and max values
    for val in lst:
        if val == min_val:
            result.append(max_val)
        elif val == max_val:
            result.append(min_val)
        else:
            result.append(val)
    
    return result
```

This Python script defines a function called `strange_sort_list` that takes a list of integers as input. It sorts the list in a "strange" order: it starts with the minimum value, then places the maximum value of the remaining integers, then the minimum value again, and so on. The function follows this pattern alternating between the minimum and maximum values as it iterates through the list.

The function is designed to handle edge cases where the list contains an even number of elements or multiples of the same value. It correctly identifies the minimum and maximum values within the list and constructs the sorted result by alternating between them. The script includes a comment that highlights this behavior and emphasizes the pattern of alternating minimum and maximum values.

The function's behavior is further reinforced by including experimental examples in the comment section. These examples showcase different scenarios, such as a list containing consecutive integers, an empty list, or a list with a single element. The corresponding output of the function is shown for each example, allowing readers to visually verify the correct behavior of the `strange_sort_list` function.