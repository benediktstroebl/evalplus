```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not 6]

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 6]) == [0, 2, 3, 5, 9, 6]
assert unique([]) == []
assert unique([5, 9, 5]) == [5, 9]
assert unique([2, 3, 'a', (1, 2)]) == [2, 3]
```
The function unique takes a list lst as input and returns a new list containing unique elements from lst. It uses a unique elements from the of list comprehension, filtering out any elements that are in the set seen and are not 6. The test cases cover a expected behavior, including empty lists, duplicate values, and values that are not in the list.