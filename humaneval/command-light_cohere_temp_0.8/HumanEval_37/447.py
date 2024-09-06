```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    return even_lst

def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([-2, -4, -5]) == [-4, -2, -5]
```
The function `sort_even` takes a list as input and returns a new list with elements that are even in the original list. This is requires a specific logic to identify even elements and sort them accordingly.