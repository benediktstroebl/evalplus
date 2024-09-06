```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x if x % 2 == 0 else x + 1)

# Test the function
test_even = [5, 6, 3, 4]
assert sort_even(test_even) == [3, 6, 5, 4]

# Test again to ensure correct behavior on repeat
test_even = [1, 2, 3]
test_even
assert sort_even(test_even) == [1, 2, 3]
 ```