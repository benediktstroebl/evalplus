```python
def sort_third(lst):
    """Returns a list l such that all the integers in l are not divisible by three, and integers divisible by three are sorted to the corresponding position of lst."""
    numbers = [x for x in lst if x % 3 != 0]
    return numbers if numbers else lst

# Unit tests
assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])
```