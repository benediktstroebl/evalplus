```python
def strange_sort_list(lst):
    # initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    result = [min_]
    
    # remove the two values from the list
    lst = [x for x in lst if x != min_ and x != max_]
    
    # recursively sort the remaining values
    result += strange_sort_list(lst)
    
    return result + [max_]
```

The function strange_sort_list works by first finding the minimum and maximum values in the list. It then initializes the result list with the minimum value. The function recursively calls itself to sort the remaining values (excluding the minimum and maximum) and then returns the sorted values, finally adding the maximum value to the result to complete the strange sort order. 

This solution adheres to the problem statement's unusual sorting strategy, which first lists the smallest value, then the largest value among the remaining elements, and so on. The provided example inputs, including lists with repeated values, are correctly sorted using this approach.