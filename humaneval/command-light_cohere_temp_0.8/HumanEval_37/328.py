```python
def sort_even(lst):
    even_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
    lst = [x for x in lst if x%2 != 0]
    return lst

# Test suite
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```