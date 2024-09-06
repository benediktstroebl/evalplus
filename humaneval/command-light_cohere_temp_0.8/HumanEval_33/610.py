```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 6, 3, 9, 8, 1])
    [1, 2, 6, 3, 8, 9, 10]
    >>> sort_third([10, 2, 6, 3, 9, 8, 1, 5])
    Traceback (most recent call last):
      File "<string>", line 6: TypeError: unsupported operand 'NoneType'
    for the list in <module='sort_third'>items()
    File "<string>", line 13: unsupported operand '=' in +
    File "<string>", line 13: 'sort_third()'
    """

```
This Python function takes a list of numbers and returns a new list with numbers from the original list at indices that are not divisible by three, in sorted order.