```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd indic, while its values at the even indices are equal to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 11, 12])
    [10, 11, 12]
    """
    # initialize a list to store sorted even elements
    even_sorted = []

    # iterate through the list
    for num in l:
        # if the number is even, append to the even_sorted list
        if num % 2 == 0:
            even_sorted.append(num)

    # join the list to get the final sorted list
    return even_sorted

```