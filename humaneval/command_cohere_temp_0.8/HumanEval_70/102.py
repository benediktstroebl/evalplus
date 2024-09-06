```python
def strange_sort_list(lst):
    """
    Do the strange sort on the list of integers.

    Strange sorting is when you start with the minimum value,
    then take the maximum of the remaining integers, then the minimum,
    and so on until you reach the greatest integer in the list.

    Parameters:
        lst (list): List of integers.

    Returns:
        list: List sorted in the strange way described above.
    """
    if len(lst) <= 1:
        return lst
    return [min(lst)] + [max(lst[:-1])] + strange_sort_list(lst[:-1])
```

The function works by starting with the minimum number and then finding the maximum number among the remaining numbers in the list. This process is repeated until all numbers are sorted in the "strange" order. The base case is when the list has 1 or 0 elements, where the list is already sorted and can be returned as is.

The approach is efficient because it uses the maximum and minimum operations that have a time complexity of O(n) each, and the overall complexity is O(n log n). Also, the approach is quite intuitive and easy to understand, which is also important in practical programming.