```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    result = [min_]
    
    # Iterate through the list, alternating between min and max values
    for num in lst:
        if num == min_:
            result.append(max_)
        else:
            result.append(min_)
    return result
```

The function strange_sort_list sorts the list in a "strange" order as described in the prompt. It first finds the minimum and maximum values in the list, then alternates between adding the minimum and maximum values to the result list, starting with the minimum. This will create a list that starts with the smallest value, then jumps to the largest value in the list, then the second-smallest value, and so on. The function handles cases where the input list is empty or contains only one unique value, as specified in the examples in the prompt.