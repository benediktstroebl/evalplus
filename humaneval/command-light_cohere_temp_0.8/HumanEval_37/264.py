```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.

    Parameters:
        l (list): the list of numbers that needs to be sorted

    Returns: list: the list of numbers that is sorted with the values at the even index kept as they are, but sorted with the odd index values.
    """

Example usage:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
```