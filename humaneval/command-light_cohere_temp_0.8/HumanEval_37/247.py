```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    even_vals = [y for y in lst if y % 2 == 0]
    return even_vals

# Test the function
test_list = [1, 2, 3, 5, 6, 3, 4]
result = sort_even(test_list)
assert len(result) == 6
assert [x for x in result] == [3, 6, 5, 4]
assert [x for x in result] == [x for x in [1, 2, 3, 4, 5, 6]]
```