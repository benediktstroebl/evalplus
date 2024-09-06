```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x % 2 == 0) and x or (not x % 2))

# Tests
test_sort_even = []
test_even = [5, 6, 3, 4]
test_odd = [1, 2, 3]

test_sort_even.add(test_even)
test_sort_even.add(test_odd)

# Check function works as expected
assert sorted(test_even) == [3, 4, 5, 6]
assert sorted(test_odd) == [1, 2, 3]
```