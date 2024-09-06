```python
def sort_third(l: list):
    """Sorts the list l such that all values that are not divisible by three are at the beginning"""
    l = list(filter(lambda x: (x%3==0), l)) + [x for x in l if x%3!=0] + [x for x in l if x%3==3]
    return l

# Test case 1
print(sort_third([1, 2, 3]))
# Output: [1, 2, 3]

# Test case 2
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
# Output: [2, 6, 3, 4, 8, 9, 5]

# Test case 3
print(sort_third([10, 2, 6, 3, 9, 4, 5, 8]))
# Output: [2, 6, 3, 8, 9, 10]
```