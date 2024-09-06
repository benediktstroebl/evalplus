```python
def sort_even(lst):
    return lst[:]  # Concatenate the list with the first element (odd index) to be sorted

# Test the function
    test_list = [5, 6, 3, 4]
    expected = [3, 6, 5, 4]
    result = sort_even(test_list)
    assert result == expected, "The function did not return the expected result."
```