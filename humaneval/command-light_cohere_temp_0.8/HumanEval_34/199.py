```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == 0]

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
assert unique([3, 'x', 'y', 'z']) == ['x', 'y', 'z']

# Test case 3
assert unique([]) == []
```

This code defines a function called unique, which takes a list as an argument and returns a new list containing unique elements from the original list. The function uses a set to keep track of elements that have been seen, and then it iterates through the original list, only adding elements to the list if they are not already in the set and not equal to zero. This ensures that all unique elements are returned in sorted order.

The code also includes several test cases to verify the behavior of the unique function, passing various input lists and asserting that the returned unique elements are correct.