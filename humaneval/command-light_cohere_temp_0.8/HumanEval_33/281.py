```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
   >>>
    l = [5, 6, 3, 4, 8, 9, 2]
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 11, 12, 13, 1, 2])
    Traceback (most recent call last):
    ...
    TypeError: 'int' object does not support item assignment (only attributes)
    ```