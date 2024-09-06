```python
def sort_third(lst):
    """Sorts a list l such that values divisible by three are sorted separately."""
    return sorted(lst, key=lambda x: (x if x % 3 == 0 else x))

#Test case 1:
assert sort_third([1, 2, 3]) == [1, 2, 3]

#Test case 2:
assert sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

#Test case 3:
assert sort_third([10, 2, 3, 4, 6, 5]) == [2, 3, 6, 4, 5, 10]
```