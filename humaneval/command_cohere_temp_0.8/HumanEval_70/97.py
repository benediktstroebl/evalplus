```python
def strange_sort_list(lst):
    result = []
    while len(lst) > 0:
        minval = min(lst)
        maxval = max(x for x in lst if x > minval)
        result.extend([minval, maxval])
        lst = [x for x in lst if x != minval and x != maxval]
    return result
```

The code sorts a list of integers in a "strange" order, it first selects the minimum value in the list, then the maximum value in the list that's left after removing the minimum, and then repeats this process. The overall time complexity is O(n log n) due to the pair of `min` and `max` operations in each iteration. The space complexity is O(1) since it only uses a constant amount of extra space.