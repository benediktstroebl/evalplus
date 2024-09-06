```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the items that are not divisible by three, while its values at
    the items that are divisible by three are equal to the values of the corresponding items, but sorted.
    """
def test(lst):
        lst = [5, 6, 3, 4, 8, 9, 2]
        expected = [2, 6, 3, 4, 8, 9, 5]
        got = sort_third(lst)
        assert lst == expected
        assert got == expected
        return True
```