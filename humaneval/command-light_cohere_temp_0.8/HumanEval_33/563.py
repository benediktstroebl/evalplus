```python
def sort_third(l: list):
    """Sorts list l such that values not divisible by three remain unchanged, while values divisible by three are sorted.
    Args:
        l: list of integers
    Returns: list, where the values at indices that are not divisible by three are left unchanged, and the values at indices divisible by three are sorted.
    """ raising an list too a
    """ be a list of integers"""

# Test
test_list = [5, 6, 3, 4, 8, 9, 2]
test_result = sort_third(test_list)
assert test_result == [2, 6, 3, 4, 8, 9, 5]

test_list = [100, 200, 3, 60, 100]
test_result = sort_third(test_list)
assert test_result == [100, 200, 3, 60, 100]

test_list = [7, 1, 2, 8, 4]
test_result = sort_third(test_list)
assert test_result == [2, 1, 4, 8, 7]
```