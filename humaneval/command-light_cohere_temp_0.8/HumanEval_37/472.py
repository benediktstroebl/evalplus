```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    # list comprehension to get even index numbers and value
    even_indicies = [x for x in range(len(l)) if l[x] % 2 == 0]
    even_values = [l[x] for x in even_indicies]

    # sort the list based on even values in ascending order
    l_sorted = [x for x in l if x in even_values] + [x for x in even_values if x not in l]
    return l_sorted
```