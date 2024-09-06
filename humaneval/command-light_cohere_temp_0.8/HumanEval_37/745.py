```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 2, 4, 8])
    [8, 10, 2, 4]
    >>> sort_even([1, 10, 3, 9])
    [1, 3, 9, 10]
    >>> sort_even([5, 3, 2, 8, 1])
    [1, 2, 8, 3, 5]
    """
    l.sort(even)
def sort_even(l: list):
        return sorted(l, key=lambda x: (x[0] if x[1] else x[1]), [0, 1])
```
This script defines a function called sort_even that takes a list l as input and returns a sorted list l'. The function uses the sorted function with a custom key function to sort the list based on even or odd indices.