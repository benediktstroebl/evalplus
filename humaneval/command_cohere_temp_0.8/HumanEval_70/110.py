```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    result = [min_]
    
    # Iterate through the list, adding the maximum value of the remaining elements to the result, followed by the minimum value of the remaining elements
    for num in lst[1:]:
        if num > max_:
            result.append(max_)
            max_ = num
        else:
            result.append(min_)
            min_ = num
    
    return result
```

The function `strange_sort_list` takes a list of integers as input and returns the list in a strange order, as defined in the prompt. The function initially finds the minimum and maximum values in the list. It then adds the minimum value to the result and updates the maximum value to be the maximum value in the remaining elements of the list. This process is repeated until all elements have been added to the result in the correct order.