Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    a = lst[0]
    for b in lst[1:]:
        if a <= b:
            # All elements are monotonically increasing
            if a == b:
                return True
            a = b
        else:
            return False
    return True
```

This script defines a Python function `monotonic` that checks whether the elements of a list are monotonic, meaning they are either monotonically increasing or decreasing. The function returns `True` if the list elements are monotonic and `False` otherwise. It handles the edge case where the list has only one or no elements, returning `True` for the former, as such a list is considered to be monotone. It iterates through the list, comparing each element to the previous one. If the current element is greater than or equal to the previous one and they are not equal, it continues iterating, treating the list as monotonically increasing. However, if the current element is less than the previous one, it returns `False`, indicating the list is not monotonically increasing. 

The function relies on an initial element, `a`, obtained from the list's first element, and performs comparisons using this reference point. This approach simplifies the comparison logic. Overall, this function provides a straightforward way to verify whether a list's elements exhibit monotonic behavior, enhancing efficiency and readability.