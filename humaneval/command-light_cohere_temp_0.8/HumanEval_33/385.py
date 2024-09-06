```python
def sort_third(l: list):
    """Sorts a list of numbers so that values divisible by three appear toward the beginning.
    The list l is not modified, but a reference to the list is returned. """

    test that the for the following inputs and expected outputs:
    [1, 2, 3] -> [1, 2, 3]
    [5, 6, 3, 4, 8, 9, 2] -> [2, 6, 3, 4, 8, 9, 5]
    [10, 11, 12] -> expected runtime error (list is too long)
    """
    return sorted(l, key=lambda x: int(x) // 3 if x % 3 == 0 else x)
```