```python
def unique(lst):
    return list(set(lst))

# Test case 1:
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2:
assert unique([]) == []

# Test case 3:
assert unique([1, 2, 3]) == [1, 2, 3]
```
This script defines a function called unique, which takes a list as input and returns a new list containing only the unique elements from the original list. The test cases are used to verify the correctness of the function, ensuring that it correctly filters out duplicates and returns the expected unique elements.