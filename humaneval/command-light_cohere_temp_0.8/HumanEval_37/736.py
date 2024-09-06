```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.
    """
def test_sort_even():
    l = [1, 2, 3]
    return sort_even(l) == [1, 2, 3]
```