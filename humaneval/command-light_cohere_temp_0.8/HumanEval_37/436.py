```python
def sort_even(lst):
    even_list = [x for x in lst if x % 2 == 0]
    return even_list if even_list != [] else [x for x in lst if x % 2 != 0]

# Test the function
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```