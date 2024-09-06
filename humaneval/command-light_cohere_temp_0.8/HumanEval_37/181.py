```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x - 1)

# Test case 1
assert sort_even([1, 2, 3]) == [1, 2, 3]

# Test case 2
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

# Test case 3
assert sort_even([10, 2, 4, 6]) == [2, 10, 4, 6]
```
The script defines a function `sort_even` that sorts a list in a way that even indices are kept in their original order, while odd indices are shifted by one. The test cases demonstrate the