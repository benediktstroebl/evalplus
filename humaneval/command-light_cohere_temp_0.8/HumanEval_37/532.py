```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x - 1)

# Unit tests
test_sort_even = unittest.TestCase("list", [1, 2, 3, 4, 5, 6])
test_result = sort_even(test_list)
assert test_result == [3, 6, 5, 4, 1, 2], "The list was not sorted correctly."
```