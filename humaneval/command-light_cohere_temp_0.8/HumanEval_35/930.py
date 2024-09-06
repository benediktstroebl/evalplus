```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test case using custom function
test_max_element = lambda: max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert test_max_element() == 123

# Another test case
test_max_element2 = lambda: max_element([1, 2, 3, 4, 5, 6])
assert test_max_element2() == 5
```