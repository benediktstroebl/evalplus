```python
def sort_third(lst):
    """Sorts the list lst such that values not divisible by three are in front, while values divisible by three are in the back."""
    return [x for x in lst if x % 3 != 0] + [x for x in lst if x % 3  == 0]

# Test case 1
print(sort_third([1, 2, 3]))  # [1, 2, 3]

# Test case 2
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]

# Test case 3
print(sort_third([11, 22, 33, 11, 99, 88, 77, 66]))  # [11, 66, 77, 88, 99, 22, 33]
```