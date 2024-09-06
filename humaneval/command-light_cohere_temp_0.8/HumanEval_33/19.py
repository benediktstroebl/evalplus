```python
def sort_third(lst):
    """Sorts the list l such that elements not divisible by three are at the beginning"""
    # Create a new list lst2 of the same elements as l
    lst2 = [x for x in lst if x % 3 != 0]
    # Reverse the list l such that elements divisible by three are at the beginning
    l = lst2[::-1]
    # Sort the list lst2 such that elements not divisible by three are at the beginning
    lst = l + lst2
    return lst

# Test cases
print(sort_third([1, 2, 3]))      # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2])) # [2, 6, 3, 4, 8, 9, 5]
```