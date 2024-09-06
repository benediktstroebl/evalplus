```python
def sort_even(lst):
    return lst[:] + [x for x in lst if x % 2 == 0] + lst[-1:]

# Test case using built-in list
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```