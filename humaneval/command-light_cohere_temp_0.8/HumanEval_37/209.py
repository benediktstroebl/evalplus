```python
def sort_even(lst):
    even_set = set(lst[::index(i, 2)::2 for i in range(len(lst))])
    lst[:] = [i for i in lst if i in even_set]
    return lst

# Test the function
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([9, 8, 7]) == [9, 8, 7]

test_sort_even()
```