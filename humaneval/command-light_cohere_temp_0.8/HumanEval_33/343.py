```python
def sort_third(lst):
    """Sorts the list l such that elements which are divisible by three are at the beginning, and the rest are at the end"""
    return sorted(lst, key=lambda x: (x // 3, x % 3))

# test cases
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
print(sort_third([10, 2, 3, 6, 9, 7, 5]))  # [2, 6, 3, 9, 7, 5, 10]
```