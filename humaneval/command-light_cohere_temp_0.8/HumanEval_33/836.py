```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 13, 7])
    Traceback (most recent call last):
      File "<string>", line 3, in <module>
    AssertionError: list index out of range: 3
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l.sort_just_thirds(l)

def sort_just_thirds(l: list):
    return [x for x in l if x % 3 == 0]
```
The function `sort_just_thirds` filters out values that are divisible by 3 and returns a new list containing only the remaining values.  This takes a is the list `l` and uses list comprehension and the `if` statement to filter out the values that are divisible by 3.