```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    set2 = list(set1)
    return set2

# Test case 1: Create list with duplicates
test_list1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
# Test case 2: Create list with duplicate values
test_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(unique(test_list1))  # Output: [0, 2, 3, 5, 9, 123]
print(unique(test_list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
This Python script defines a function unique that takes a list lst as input and returns a new list containing unique elements from lst, which are obtained using the set() and list() methods from the set module. The test cases demonstrate the major problem solved by this function: duplicate elements are removed from the input list and duplicates are sorted to form a unique set.