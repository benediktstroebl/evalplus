```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    return l[:] + [x if x % 2 == 0 else x[::-1] for x in l[1:]]

# Unit tests
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

```

The function 'sort_even' takes a list as input and returns a new list where the values at the even index are equal to the values of the even index of the original list, while the values at the odd index are identical to the corresponding value in the original list but are sorted.  This the also that the code block of the problem.

The unit tests check that the function works correctly.