```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    return [x for x in l if x % 3 != 0] + [x for x in l if x % 3 != 0]

# Test the function
def test_sort_third():
    input_list = [1, 2, 3, 5, 6, 8, 9]
    expected_list = [2, 6, 3, 4, 8, 9, 5]
    result_list = sort_third(input_list)
    assert result_list == expected_list
```