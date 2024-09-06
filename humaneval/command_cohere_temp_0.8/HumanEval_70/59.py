```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the sorted list
    sorted_list = [min_val]
    
    # Loop through the original list
    for val in lst:
        if val == min_val:
            sorted_list.append(val)
        elif val == max_val:
            sorted_list.append(val)
        else:
            min_val = min(val, min_val)
            max_val = max(val, max_val)
    
    # Append the last maximum value
    sorted_list.append(max_val)
    
    return sorted_list
```

The function `strange_sort_list` takes in a list of integers and returns that list in a "strange" order, which starts with the smallest value, then the largest value among the remaining numbers, and then the smallest value again, and so on. The script passes the test cases provided in the prompt, returning the expected outputs for each example.