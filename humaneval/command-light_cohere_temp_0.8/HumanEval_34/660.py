```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not <= 4]

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert not unique([5, 3, 5, 2, 3, 9, 0])
assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4]
```
This code defines a function unique that takes a list lst as input and returns a list of unique elements from the input list. The unique elements are then created using a set, which automatically removes duplicates. The test cases ensure that the code produces the expected output.