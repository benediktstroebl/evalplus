```python
def sort_even(l):
    even = [e for e in l if e % 2 == 0]
    odd = [e for e in l if e % 2 != 0]
    return even + sorted(even) + odd
```

The function `sort_even` takes a list `l` as input and returns a list `l'` which has the same elements at odd indices as `l` and sorted elements at even indices. To achieve this, we use list comprehensions to split `l` into two lists: one with even indices and one with odd indices. We then return the concatenation of these two lists plus the sorted version of the even index list.

Here is a test case that verifies the function:
```python
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([0, 2, 2, 4, 6, 1]) == [0, 1, 2, 2, 4, 6]
```