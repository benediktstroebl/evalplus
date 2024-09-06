```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
            return result
    return result

# Test 1: Unique elements from an empty list
test_empty = unique([])
assert len(test_empty) == 0

# Test 2: Unique elements from a list with duplicates
test_normal = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert len(test_normal) == 6

# Test 3: Unique elements from a list with 0
test_zero = unique([0])
assert len(test_zero) == 1

# Test 4: Unique elements from a list with only one element
test_single = unique([42])
assert len(test_single) == 1

# Test 5: Unique elements from a list with nested list
test_nested = unique([(42, 'a'), (24, 'b'), (99, 'c')))
assert len(test_nested) == 3

# Test 6: Unique elements from a list with complex types
test_complex = unique([True, [42, 24], 'abc'])
assert len(test_complex) == 3
```
The function `unique` returns a list with unique elements from the input list. It utilizes a array's set data structure to keep track of seen elements, then it loops through the input list, checking each item against the set to see if it has already been seen.