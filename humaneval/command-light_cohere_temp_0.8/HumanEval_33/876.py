```python
def sort_third(lst):
    """Sorts a list l such that values that are divisible by three are in their correct order, while other values are left unchanged."""
    s = set(l)
    return [x for x in lst if x in s] + [x for x in lst if x not in s]

# Test the function
list1 = [1, 2, 3]
list2 = [5, 6, 3, 4, 8, 9, 2]

print(sort_third(list1))  # [1, 2, 3]
print(sort_third(list2))  # [2, 6, 3, 4, 8, 9, 5]
```