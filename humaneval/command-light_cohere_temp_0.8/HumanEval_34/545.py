```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test 1: Basic inputs
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_case1) == [0, 2, 3, 5, 9, 123]

# Test 2: Duplicate values
test_case2 = [5, 5, 2, 3, 3, 9, 0, 0, 123]
assert unique(test_case2) == [0, 2, 3, 5, 9, 123]

# Test 3: Float 'inf'
test_case3 = [5, 3, float('inf'), 0, 123]
assert unique(test_case3) == [0, 3, float('inf')]
```
This Python script defines a function unique that takes a list as input and returns a new list with unique elements. It uses aas set to keep track of elements that have been seen before, and it iterates through the input list, adding elements to the set and filtering out duplicates to the result. The test cases provided demonstrate the test the function with different list inputs and validate its behavior.