```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not  float('inf')]

# Test 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test 2
assert unique([]) == []

# Test 3
try:
    unique([-5])
except AssertionError as e:
    assert str(e) == "List must not be empty"

# Test 4
try:
    unique([5, 5])
except AssertionError as e:
    assert str(e) == "All elements must be distinct"
 ```