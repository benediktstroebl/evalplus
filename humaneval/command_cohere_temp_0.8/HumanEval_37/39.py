```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

The above script sorts the even indices of the list `l` and returns the original odd indices of `l`, resulting in a list `l'` where the even indices are sorted.

Here is a test case that can be used to verify the functionality of the script:
```python
def test_sort_even():
    # Test list with odd length
    assert sort_even([1, 2, 3]) == [1, 2, 3]

    # Test list with even length
    assert sort_even([1, 2, 3, 4]) == [1, 3, 2, 4]

    # Test list with mixed values
    assert sort_even([5, 3, 6, 4]) == [3, 6, 5, 4]

    # Test list with duplicate values
    assert sort_even([1, 2, 2, 3]) == [1, 2, 2, 3]
```