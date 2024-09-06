```python
def strange_sort_list(lst):
    # Calculate the minimum and maximum values in the list
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

The code sorts a list of integers in a "strange" order, where it first outputs the smallest value, then the largest value among the remaining integers, and then the smallest value again, and so on. It achieves this by iterating through the list, keeping track of the minimum and maximum values found so far. The result list is initially built with the first minimum and maximum values, and then alternating min and max values are appended to it on each iteration until all integers have been processed.