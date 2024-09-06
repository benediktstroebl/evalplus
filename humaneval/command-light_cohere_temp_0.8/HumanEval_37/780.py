```python
def sort_even(lst):
    return lst[:] if len(lst) % 2 == 0 else lst[:(len(lst) + 1) // 2]

# Test cases for the sort_even function
test_sort_even = [
    ([1, 2], [5, 6], [3, 4]),
    ([5, 6], [1, 2, 3]),
    ([1, 2, 3, 4, 5, 6])
]

# The results should be sorted lists with odd first
for test in test_sort_even:
    assert sorted(test) == test[1:]
```