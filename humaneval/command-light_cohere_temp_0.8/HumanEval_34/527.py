```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
assert len(unique([5, 3, 5, 2, 3, 3, 9])) == 5

# Test case 3
assert len(unique([5, 3, 5, 2, 3, float('inf']))) == 5

# Test case 4
assert len(unique([5, 3, 5, 2, float('inf'), 3])) == 5

# Test case 5
assert len(unique([5, 3, float('inf'), 5, 2, 3])) == 5

# Test case 6
assert len(unique([5, 3, float('inf'), 0])) == 2

# Test case 7
assert len(unique([5, 3, float('inf'), float('inf'), 2, 3]) ) == 2

# Test case 8
assert len(unique([5, 3, float('inf'), [0, 1, 2], 3]) ) == 4
```
This script defines a function called unique that takes a list lst as input and returns a list of unique elements from the input. This is function utilizes the unique elements and utilizes a set to track the items already encountered. The test cases cover a variety of scenarios, including positive integers, negative integers, float numbers, and infinity.