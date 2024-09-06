```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]

    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]

    >>> sort_third([10, 2, 15, 3, 7])
    Traceback (most recent call last):
      File "<string>", line 3, in <module>
        assert not divisible(3, x) for x in l
      File "<ipython-input-file-node>", line 13, in <module>
        assert not divisible(3, x) for x in l
      File "<ipython-input-file-node>", line 18, in <module>
        raise AssertionError(to_str())

    AssertionError: lists 3, 7 are not divisible by 3
        ```