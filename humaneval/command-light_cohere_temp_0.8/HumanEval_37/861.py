```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else -1) * (x + 1))

# Unit tests
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```  This script defines a function `sort_even` that takes a list and sorts its elements in such a way that the odd indices will preserve their original order, while the even indices will be sorted in ascending order. 

The function then uses the `sorted` function with a custom key lambda function. The lambda function returns -1 if the index is even, -1 if it's odd, and the sum of 1 and the index. This ensures that even indices will be sorted in ascending order, and the odd indices will stay in their original order.  The final sorted list will be returned.