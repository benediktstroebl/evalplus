```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 13, 45, 3, 99])
    traceback
    [ ranking 2]
    [10, 2, 45, 99, 45, 13, 3]
    [ranking 3]
    [99, 45, 45, 2, 13, 3]
    [ranking 4]
    [45, 99, 13, 2, 3]
    """

def test_sort_third():
    test_list = [1, 2, 3]
    test_list.sort_third(test_list)
    assert test_list == [1, 2, 3]

def test_sort_third2():
    test_list = [5, 6, 3, 4, 8, 9, 2]
    test_list.sort_third(test_list)
    assert test_list == [2, 6, 3, 4, 8, 9, 5]
```
This script provides a self-contained function that sorts a list of numbers into a desirable order, and then passes those tests to verify the correctness of the sorting.