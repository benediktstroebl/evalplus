```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 1, 2, 3])
    Traceback (most recent call last):
    ...
    TypeError: 'list' object does not support item assignment  (index 4)
    ...
    ...
    Current oral stack (most recent call last):
      <__main__ at ...>
```
The function `sort_third` will return a list that is identical to the input list in terms of values, except that all the values at indices divisible by three are replaced with the corresponding values of the list.