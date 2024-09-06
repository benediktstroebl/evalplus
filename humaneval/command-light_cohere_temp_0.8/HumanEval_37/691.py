```python
def sort_even(l: list):
    """Sorts the list l such that the values at even indices are equal to the values of the even indices of the original list, but in sorted order."""
    l = list(map(lambda x: x if x % 2 == 0 else x + 1, l))
    return l
# tests
print(sort_even([1, 2, 3]))      # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))    # [3, 6, 5, 4]
print(sort_even([10, 20, 30, 40])) # [40, 30, 20, 10]
```