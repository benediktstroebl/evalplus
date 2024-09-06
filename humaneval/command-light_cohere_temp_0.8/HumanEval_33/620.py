```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([11, 22, 33, 99])
    Traceback (most recent call last):
      File "<string>", line 4, in <module>
    TypeError: 'list' object does not support item assignment
    """
def test_sort_third(test_list):
    test_list = [3, 6, 2, 1, 4, 9]
    test_list = sort_third(test_list)
    assert test_list == [2, 6, 3, 4, 8, 9, 5]
```