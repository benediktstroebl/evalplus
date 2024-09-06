```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x if x % 2 == 0 else x+1)

# Test cases
test_list = [1, 2, 3, 6, 5, 4]
assert sort_even(test_list) == [3,6,5,4,1,2]

test_list_mixed = [5, 6, 3, 4, 1, 2]
assert sort_even(test_list_mixed) == [3,6,5,4,1]

test_empty = []
assert sort_even(test_empty) == []
```