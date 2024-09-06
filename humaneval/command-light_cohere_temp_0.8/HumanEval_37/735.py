```python
def sort_even(lst):
    # Sort list keeping even numbers as they are, and preserving their order.
    return sorted(lst, key=lambda x: x % 2)

# Test cases
test_list = [1, 2, 3, 4, 5, 6]
assert sort_even(test_list) == [1, 2, 3, 4, 5, 6]

test_list2 = [5, 6, 3, 4]
assert sort_even(test_list2) == [3, 6, 5, 4, 5]

test_list3 = [1, 2, 3]
assert sort_even(test_list3) == [1, 2]

test_list4 = [5, 6, 3, 4, 7]
assert sort_even(test_list4) == [3, 6, 5, 4, 7]
```