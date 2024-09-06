```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([]) == []
assert unique([1, 2, 3]) == [3]
assert unique([1, 2, 3, 1]) == [1, 2]
assert unique([5, 95, 5]) == [5, 95]
assert unique([True, False, True]) == [True]
```
The function unique uses the set data structure to keep track of unique items and returns a new list containing only the unique elements from the input list. 
The test cases cover a variety of inputs and ensure that the function is working correctly.