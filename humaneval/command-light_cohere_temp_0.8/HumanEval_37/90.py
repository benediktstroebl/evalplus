```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x if x % 2 == 0 else x + 1)

# Test suite
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
```  This script defines a function **sort_even** that sorts even numbers in a list while keeping the odd numbers as they are. It then tests the transport this approach to sort even numbers efficiently and correctly.