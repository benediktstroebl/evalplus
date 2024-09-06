```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test case 1: Verify function returns expected unique elements
test_unique = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_unique) == [0, 2, 3, 5, 9, 123]

# Test case 2: Verify no duplicates with infinite input
infinity = float("inf")
assert unique( [x for x in infinity]) == [infinity]
```
This script defines a function `unique` that takes a list as input and returns a new list with unique elements. It uses a unique elements and set difference to efficiently identify unique elements.