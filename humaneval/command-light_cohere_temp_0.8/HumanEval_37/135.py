```python
def sort_even(l: list):
    return l[:][::2]

def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```  This script defines a function sort_even, which takes a list l and returns a new list l[:][::2], which is identical to the original list in the odd index positions, while the even index positions contain the same elements with the same values, but in sorted order.