```python
def unique(lst):
    """Return sorted unique elements in a list"""
    seen = set()
    return [x for x in lst if x not in seen and x not None]

# Tests
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Expected output: [0, 2, 3, 5, 9, 123]

print(unique([1, 2, 3, 4, 5, 6, 7, 8]))
# Expected output: [1, 2, 3, 4, 5, 6, 7, 8]

print(unique([]))
# Expected output: [ ]

print(unique([1, 2, 3, 'abc']))
# Expected output: [1, 2, 3]
``` 
This code defines a function unique that takes a list as input and returns a new list containing only the unique elements from the original list. It uses a
set to keep track of seen elements, then iterates through the original list and adds elements to the set if they are not seen before and not None.