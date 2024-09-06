```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x % 2)

# Test the function with some examples
assert(sort_even([1, 2, 3]) == [1, 2, 3])
assert(sort_even([5, 6, 3, 4]) == [3, 6, 5, 4])
assert(sort_even([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6])
```