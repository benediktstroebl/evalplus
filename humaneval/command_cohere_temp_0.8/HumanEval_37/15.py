```python
def sort_even(l: list):
    even = [e for e in l if e % 2 == 0]
    odd = [o for o in l if o % 2 != 0]
    even = sorted(even)
    return odd + even
```

The function `sort_even` takes a list `l` and returns a list `l'` which has the same elements at odd indices as `l` and sorted elements at even indices. The function utilizes list comprehensions to separate the even and odd indices, sorts the even indices, and then returns the odd indices as well as the sorted even indices.

Here is a test suite to ensure the function behaves as expected:
```python
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([0, 7, 2, 1]) == [0, 1, 2, 7]
    assert sort_even([-2, -1, 0, 1]) == [-2, -1, 0, 1]
    assert sort_even([3, -1, -2, 0, 1]) == [3, -1, -2, 0, 1]
```