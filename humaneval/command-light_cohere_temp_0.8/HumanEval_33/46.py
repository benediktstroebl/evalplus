```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 1, 2, 20, 30])
    [10, 1, 2, 20, 30]
    >>> sort_third([10, 1, 2, 20, 30, 10])
    [10, 1, 2, 20, 30, 10]
    >>> sort_third([])
    Traceback (most recent call last):
      File "<string>", line 7: raise attribute error: list object: None
```
The function takes a list `l` and returns a new list `l'` where the values of the indices that are divisible by three are equal to the corresponding values of `l`, but are sorted. 

This is achieved through the `islic` function that identifies if an index `i` is divisible by three. If it is, then the corresponding value at `i` is returned as is. If it is not, the value is returned sorted by `sorted` function.