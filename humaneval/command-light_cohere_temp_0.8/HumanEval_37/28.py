```python
def sort_even(lst):
    even_list = [x for x in lst if x % 2 == 0]
    return even_list

def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

# Your code here!
```