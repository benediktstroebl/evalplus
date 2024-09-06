```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    return [x for x in l if x != 3 and x % 3 == 0] + [x for x in l if x == 3]

# Tests
def test_sort_third():
    tests = [
        [1, 2, 3],
        [5, 6, 3, 4, 8, 9, 2],
        [10, 2, 3]
    ]

    expected = [1, 2, 3]
    got = sort_third(tests)
    assert got == expected
```