```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

The function `sort_even` takes a list `l` as an argument and returns a list `l'` such that `l'` contains the same elements as `l` at odd indices, and the elements at even indices of `l'` are equal to the elements at even indices of `l`, but sorted in ascending order. 

Here is an example of how the above function can be tested:
```python
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([1, 4, 3, 7, 2]) == [1, 3, 2, 4, 7]
```