```python
def sort_even(lst):
    even_set = set(lst[::index:: even])
    return [::index] + [x for x in lst if x in even_set]

# Test case: pass test function with list of integers
test_sort_even = lambda: all(sort_even([1, 2, 3])) == [1, 2, 3]
# test_sort_even()
```