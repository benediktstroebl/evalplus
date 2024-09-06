```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x // 2, x % 2))

# Unit tests
test_sort_even = unittest.TestCase('list', [1, 2, 3, 4, 5, 6])
test_sort_even.check()
# [2, 3, 4, 5, 6], [(1, 2), (3, 4), (5, 6), (4, 3)]
# pass
```