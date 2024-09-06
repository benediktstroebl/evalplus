```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 58])
    Traceback (most recent call last):
      File "<string>", line 4, in <module>
        assert len(l) > 2
      File "<string>", line 9, in sort_third
    AssertionError:  list has only 3 items rather than >= 4
    """
```