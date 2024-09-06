```python
def sort_third(lst):
    """This function sorts a list l according to the criteria that numbers not divisible by three come first, and numbers divisible by three are left unchanged. Numbers less than corresponding to the values of l that are divisible by three, and numbers greater than those values are sorted accordingly.

    Returns a value of a sorted list l' where l is a list of numbers.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    lst[:] = [x for x in lst if x % 3 != 0]
    return list(sorted(lst))
```