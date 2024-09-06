```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 20, 30, 40])
    [40, 30, 20, 10]
    """
    l.sort_even([1, 2, 3])
    print(f"Sorted even: {sorted([1, 2, 3])}")
    print(f"Sorted odd: {sorted([3, 6, 5, 4])}")
    ```

This script defines a function named sort_even that takes a list l as an argument. The function sorts the same elements of the list and returns the sorted even elements in the original list.