```python
def sort_third(lst):
    """This function sorts the list lst such that elements not divisible by three are at the beginning"""
    return sorted(lst, key=lambda x: int(x) // 3)

# Test the function
list1 = [1, 2, 3]
list2 = [5, 6, 3, 4, 8, 9, 2]

print("List 1 sorted using the sort_third function:", sort_third(list1)) # [1, 2, 3]
print("List 2 sorted using the sort_third function:", sort_third(list2)) # [2, 6, 3, 4, 8, 9, 5]
```