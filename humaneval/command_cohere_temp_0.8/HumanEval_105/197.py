```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
        9: 'Nine'
    }
    result = [transf_map[int(i)] for i in sorted_arr if i in transf_map]
    return result if result else []
```

The following tests will check if the function correctly handles the different scenarios:
```python
def test_by_length_valid():
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    assert by_length([]) == []
    assert by_length([1, -1, 55]) == ['One']
    assert by_length([10, 11, 12]) == []
```