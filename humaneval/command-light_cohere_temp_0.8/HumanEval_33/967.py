```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    third decimal place, while its values at decimal places 0, 1, 2 are sorted.
    >>> sort_third([1, 2, 3])
    [1,3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2,6,3,4,8,9,5]
    >>> sort_third([1,2,3,4,5,6,7])
    [2,3,4,5,6,7]
    >>> sort_third([0.2,1,00])
    [0.2, 1,00]
    """

The function uses the built-in sorting function and then takes the third decimal place of each number.