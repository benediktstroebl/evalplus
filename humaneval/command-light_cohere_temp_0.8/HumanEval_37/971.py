```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    even.sort()
   
             return even
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([10, 20, 30]) == [10, 20, 30]
```