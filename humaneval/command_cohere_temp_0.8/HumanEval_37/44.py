```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

The function `sort_even` takes a list as an argument and returns a list with the even indices holding the same value as in the original list, but sorted, while the odd indices remain unchanged. To achieve this, the function slices the list into pairs of even and odd indices with the `even = l[::2]` and `odd = l[1::2]` lines, respectively. The list of even indices is then concatenated with the sorted list of odd indices to return the desired list.

Here is a test suite to ensure that the function behaves as expected:
```python
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([0, 7, 8, 9]) == [0, 7, 8, 9]
    assert sort_even([10, 11, 12, 13, 14]) == [10, 12, 11, 13, 14]
    assert sort_even([15, 20, 21, 22, 16, 17, 18, 19]) == [15, 16, 17, 18, 19, 20, 21, 22]
```

This test suite contains multiple test functions to validate the behavior of `sort_even` against different input list variations. Each test function checks if the returned list matches the expected output using the `assert` statement.