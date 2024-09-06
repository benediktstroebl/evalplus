```python
def strange_sort_list(lst):
    # Sort the list, but always keep the minimum value at the first position
    if len(lst) == 0:
        return lst
    min_val = min(lst)
    max_except_min = max(x for x in lst if x != min_val)
    return [min_val, max_except_min, strange_sort_list(lst[:len(lst) - 1])]
```

This code works by first finding the minimum and maximum values in the list, except for the minimum value. It then recursively sorts the rest of the list, placing the maximum value in the second spot. This process repeats until the list is sorted. 

This solution utilizes Python's list comprehension, and recursive functions.