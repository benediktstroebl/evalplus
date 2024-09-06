```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not  float('inf')]

# Test 1: Basic inputs
print("Test 1: ", unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Expected Output: [0, 2, 3, 5, 9, 123]

# Test 2: Duplicate values
print("Test 2: ", unique([5, 3, 5, 3, 7, 7, 9, 0, 123]))
# Expected Output: [0, 3, 5, 7, 9, 123]

# Test 3: Float inputs
print("Test 3: ", unique([5, 3, 5, 3. encountered, float('inf'), 'abc']))
# Expected Output: [5, 3, 3]

# Test 4: Empty list
print("Test 4: ", unique([]))
# Expected Output: []
```

This function unique takes a list as an input and returns a new list containing only the unique elements from the input. The function utilizes a set to keep track of the unique elements. The function then iterates through the list, and adds each element to the set. Finally, the function returns a new list with the unique elements from the original list.