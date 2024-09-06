```python
def unique(lst):
    """Return sorted unique elements in a list"""
    unique = set(lst)
    return list(unique)

# Test cases
TestCases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 9, 2],
    [3, 'three'],
    ['abc', 'def'],
    [123, 456, 789]
]

# Function calls
for testCase in TestCases:
    print(unique(testCase))
``` 
This code defines a Python function called unique that takes a list as input and returns a new list containing only the unique elements from the original list. The unique set of elements and then converts it back to a list. This function can be easily used to solve the problem of returning unique elements from a list and can be easily called with different test cases to verify its correctness.