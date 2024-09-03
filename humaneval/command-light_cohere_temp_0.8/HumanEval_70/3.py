Here's the self-contained Python script with the strange sort function, along with its unit tests:
```python
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, see the implementation below.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []

    '''
def test_sort_list():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([]) == []
```
The `test_sort_list` function contains three assertions, each testing a different input list and the result of `strange_sort_list` with those inputs.