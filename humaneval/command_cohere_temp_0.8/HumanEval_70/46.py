```python
def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers.

    Strange sorting, is when you start with the minimum value,
    then take the maximum of the remaining integers, then the minimum,
    and so on until you have passed through all the numbers.
    """
    if not lst:
        return lst
    return [min(lst[1:]) for _ in range(len(lst))] + strange_sort_list(lst[1:])
```

The code exploits the fact that the desired permutation of the list [min value, max value, min of remaining, max of remaining, ...] is reproducibly constructed by repeatedly taking the minimum value from the remaining elements (those with higher values than the current minimum). The result of this process is concatenated to the end of the result for the remaining elements, and this is repeated until all elements have been considered as minima.