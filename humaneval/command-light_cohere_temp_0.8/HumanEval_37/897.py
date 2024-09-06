```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    return l[: len(l) // 2] + [x + y for x, y in zip(l[:: len(l) // 2], l[len(l) // 2:])]

#unit tests
def test_sort_even():
    tests = [
        [1, 2, 3],
        [5, 6, 3, 4],
        [5, 6, 7, 2],
        [10, 9, 8, 7]
    ]
    
    for test_set in tests:
        actual = sort_even(test_set)
        expected = [3, 6, 5, 4]
        assert actual == expected, f"Checking {test_set} failed"

#run the tests
test_sort_even()
```