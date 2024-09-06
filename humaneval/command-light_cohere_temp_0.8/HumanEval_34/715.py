```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted(set(l), key=lambda x: x)

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
empty_list = []
assert unique(empty_list) == [] 

# Test case 3
 duplicate_elements = [3, 3, 5]
list1 = [1, 2, 3, 4, 3, 5, 3]
assert unique(list1) == [1, 2, 4, 5]
 ```

This script defines a function `unique` that takes a list as input and returns a new list containing only the unique elements from the input. It utilizes the particular sorted set to remove duplicates and maintain the sorted order.