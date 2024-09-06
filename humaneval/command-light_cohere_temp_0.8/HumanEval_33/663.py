```python
def sort_third(lst):
    """This function sorts a list l such that the elements not divisible by three are moved towards the beginning and the end of the list, while the elements divisible by three are sorted normally.

    : Input: list l (sorted list of numbers)
    Return: list l' (sorted list of numbers)

    >>> sort_third([1, 2, 3])
    [1, 3, 2]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 11, 12, 13, 1, 20, 30])
    [1, 10, 11, 12, 13, 20, 30]
    >>> sort_third([1, 2, 3, 4, 5, 6, 7])
    Error: list is empty
    >>> sort_third([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
    [18, 19, 20, 21, 16, 17, 15, 14, 13, 12, 11, 10, 9, 8, 7]
```