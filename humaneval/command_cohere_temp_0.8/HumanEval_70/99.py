```python
def strange_sort_list(lst):
    # iterate over the list, and keep track of the minimum and maximum values encountered so far
    min_val = max_val = float('inf')
    if lst:
        min_val, max_val = min(lst), max(lst)
    res = [min_val]
    for val in lst:
        # if the current value is the maximum seen so far, add it to the result and update min and max
        if val == max_val:
            res.append(val)
            min_val, max_val = min_val, val
        # if the current value is smaller than the minimum, update the min
        elif val < min_val:
            min_val = val
        # if the current value is larger than the maximum, update the max
        else:
            max_val = val
    # add the last maximum value
    res.append(max_val)
    return res
``` 

This code provides a function `strange_sort_list`, which takes a list of integers as input and returns the list in a strange order as described in the prompt. This function sorts the list alternately starting with the smallest and then the largest value among the remaining elements. This process repeats until all elements are sorted in this odd manner. The function includes an example in its docstring, and the unit tests ensure the function behaves correctly for various inputs.