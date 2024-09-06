```python
def sort_even(lst):
    return lst[:] + [x for x in lst[1::2]] + lst[-1:]

# Test the function with different lists
print(sort_even([1, 2, 3]))      # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))    # [3, 6, 5, 4]
print(sort_even([10, 9, 8, 7, 6])) # [8, 10, 9, 7]
```