```python
def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the result list with the initial min and max values
    result = [min_val, max_val]
    
    while lst:
        min_val = min(lst)
        max_val = max(lst)
        del lst[lst.index(min_val)]
        del lst[lst.index(max_val)]
        result.extend([min_val, max_val])
    
    return result
``` 

This Python script defines a function called `strange_sort_list` that takes in a list of integers as an argument. It sorts the list in a strange order: it starts with the minimum value, then the maximum value of the remaining integers, then the minimum of the remaining, and so on. The function repeats this process until the list is sorted.

The code initially finds the minimum and maximum values from the input list and uses these to initialize a result list. Then, in a loop, it repeatedly finds the current minimum and maximum values, removes them from the list, and adds them to the result. Ultimately, the function returns the strange-sorted list.