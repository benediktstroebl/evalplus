```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted."""
    return sorted(l, key=lambda x:x if x%2==0 else x-1)

# Unit tests
def test_sort_even():
    test_list = [1, 2, 3]
    test_result = sort_even(test_list)
    assert test_list == test_result
    test_list = [5, 6, 3, 4]
    test_result = sort_even(test_list)
    assert test_list == [3, 6, 5, 4]
```