```python
def strange_sort_list(lst):
    """
    Do a strange sort of a list - return it in order of min, max, min, max,...
    """
    res = []
    while len(lst) > 1:
        res.append(min(lst))
        res.append(max(filter(lambda x: x != res[-1], lst)))
        lst = [x for x in lst if x != res[-1] and x != res[-2]]
    if lst:
        res.extend(lst)
    return res
```

The logic behind the strange sorting is to start with the smallest number as the first element of the result. Then, from the remaining numbers, we pick the largest. Then, for the new remaining numbers, we again pick the smallest, and so on. The resulting order is `[min, max, min, max, ...]`.

Such sorting has specific use cases in algorithms like Priority Queue or certain graphical distributions. 

This algorithm has a time complexity of `n log(n)` because it uses both `min` and `max` operations on a list of size `n`, which can be done in logarithmic time. Also, it has a space complexity of `n` as it creates an extra list of size `n`.