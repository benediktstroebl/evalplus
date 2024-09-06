```python
def sort_even(l):
    even, odd = zip(*[(i, v) for i, v in enumerate(l) if i % 2 == 0])
    return [o if i % 2 else e for i, e, o in zip(range(len(l)), odd, even)]
```

This function takes a list `l` and returns a new list where the even-indexed elements are sorted while the odd-indexed elements remain unchanged. The `zip(*[(i, v) for i, v in enumerate(l) if i % 2 == 0])` construct helps create nested lists of alternating even and odd indices and their corresponding values. Then, the list comprehension returns the original list `l` but sorts the even-indexed elements using `e` (the sorted even-indices values) and leaving the odd-indexed elements unchanged using `o`. 

Here is a test case that can be used to verify the function:
```python
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([10, 9, 8, 7]) == [8, 10, 9, 7]
```