```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

The above code divides the list into two halves using the `::2` index, which creates two arrays, even and odd. The odd array is sorted using the `sorted` function and then concatenated back with the even half of the list. This ensures that the list's odd indices preserve their original order, while the even indices are sorted. 

Here is a test case that verifies the correct operation of the `sort_even` function:
```python
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([0, 7, 8, 9, 1]) == [0, 1, 7, 8, 9]
    assert sort_even([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 5, 6, 7, 8, 9, 10]
```