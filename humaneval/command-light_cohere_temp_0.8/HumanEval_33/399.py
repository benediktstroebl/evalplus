```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    Test suite:
    """
    test_suite"""
    assert sorted(l) == [2, 6, 3, 4, 8, 9, 5]
    assert sorted(l, key=lambda x: x % 3) == [1, 2, 3, 4, 8, 9, 5]
    return sorted(l, key=lambda x: x % 3)
```