```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    return sorted(l, key=lambda x: x // 3)

# Test suite for function
def test_sort_third():
    test_list = [5, 6, 3, 4, 8, 9, 2]
    expected = [2, 6, 3, 4, 8, 9, 5]
    got = sort_third(test_list)
    assert expected == got
```