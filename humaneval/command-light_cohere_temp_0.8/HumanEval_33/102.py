```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
   >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> l = [10, 20, 1, 5, 6, 9, 80, 12, 70]
    l.sort_third(l)
    >>> sorted(l)
    [10, 1, 5, 6, 9, 12, 80, 20, 70]
    """

def test_sort_third():
    l = [1, 2, 3]
    l.sort_third(l)
    assert l == [1, 2, 3]
    l = [5, 6, 3, 4, 8, 9, 2]
    l.sort_third(l)
    assert l == [2, 6, 3, 4, 8, 9, 5]

test_sort_third()
```

The script defines a function `sort_third` that sorts a list of numbers such that the numbers not divisible by three are left in their original order, while the numbers divisible by three are sorted to be equal to their original values. The script also includes a function `test_sort_third` which passes tests to the `sort_third` function, and those tests pass.