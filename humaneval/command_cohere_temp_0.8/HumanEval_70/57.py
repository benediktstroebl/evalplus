```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for i,x in enumerate(lst) if i != min_idx]
    return out
``` 

The code solves the problem by using a loop. It starts by creating an empty list `out`, which stores the sorted result. Then, it keeps iterating through the original list `lst`, finding the index of the minimum value in the list, adding it to `out`, and removing it from the list. This process continues until `lst` is empty, and the `out` list contains the sorted integers in the desired "strange" order. 

The code uses append to add the minimum value to the end of the list out [], and the list comprehension to filter out the minimum value from the list lst.