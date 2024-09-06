```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [5, 3]]

# Test 1: [5, 3, 5, 2, 3, 3, 9, 0, 123] -> [0, 2, 3, 5, 9, 123]
# Test 2: [] -> []
# Test 3: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Test 4: ([1, 2], 3, [4, 5]) -> [1, 2, 3, [4, 5]]
# Test 5: [a, b, c] -> Set([a, b, c])
```  This function unique is self-contained and takes a list as input. It returns a unique elements in the list, which are the elements that are not in the set seen and not [5, 3]. 

The function uses the set seen to keep track of the unique elements. This ensures that duplicates are not added more than once to the result.