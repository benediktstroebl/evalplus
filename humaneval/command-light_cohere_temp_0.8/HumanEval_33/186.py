```python
def sort_third(lst):
    return sorted(lst, key=lambda x: int(x) // 3 if x.isdigit() else x[:-1])

# Test suite for the function
def test_sort_third(test_list):
    assert sorted(test_list, key=lambda x: int(x) // 3 if x.isdigit() else x[:-1]) == test_list, "Test failed"
    assert isinstance(test_sort_third(test_list), list), "Function returned unexpected type"

# Example usage
test_list = [5, 6, 3, 4, 8, 9, 2]
test_sort_third(test_list)
```