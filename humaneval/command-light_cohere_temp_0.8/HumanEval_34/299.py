```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0, ]]

# Tests
assert(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123])
assert(unique([]) == [])
assert(unique([21]) == [21])
assert(unique([21, 13, 21]) == [21])
assert(unique([21, 21]) == [21])

```
This code defines a function called unique which takes a list lst as input and returns a list of unique elements from the input. It uses a unique set of elements and returns the same. The function is then tested using various test cases.