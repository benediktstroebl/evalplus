```python
def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers.

    Strange sorting, is when you start with the minimum value,
    then take the maximum of the remaining integers, then the minimum,
    and so on until you reach the greatest integer in the list.

    Parameters:
        lst (list): List of integers.

    Returns:
        list: List sorted in the strange way.
    """
    if len(lst) == 0:
        return lst
    min_val = min(lst)
    max_remainder = max(lst[:len(lst) - 1])
    return [min_val, max_remainder, *strange_sort_list(lst[len(lst) - 1:]]);
```

The code exploits the fact that `max()` and `min()` functions can accept generators as arguments, thus, with each step we reduce the list length by one and operate only on the remaining elements.