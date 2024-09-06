```python
def sort_even(l: list):
    return sorted(l, key=lambda x: int(x) % 2)

# Test cases
test_list = [1, 2, 3, 4, 5, 6]
assert sort_even(test_list) == [1, 2, 3, 4, 5, 6]

test_list2 = [5, 6, 3, 4]
assert sort_even(test_list2) == [3, 6, 5, 4, 2]

test_list3 = [1, 2, 6, 3, 4]
assert sort_even(test_list3) == [2, 3, 6, 4, 1]
```