```python
def sort_even(lst):
    return sorted(lst, key=lambda x: (x + 1) % 2)

# Test cases
test_list = [1, 2, 3]
assert sort_even(test_list) == [1, 2, 3]

test_list = [5, 6, 3, 4]
assert sort_even(test_list) == [3, 6, 5, 4]

test_list = [10, 20, 30, 40]
assert sort_even(test_list) == [10, 20, 30, 40]

test_list = [5, 6, 7, 8]
assert sort_even(test_list) == [5, 6, 7, 8]
```