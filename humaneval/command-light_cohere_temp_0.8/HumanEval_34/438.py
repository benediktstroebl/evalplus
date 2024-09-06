```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float('inf')]

# Test the function with a list of elements
# Ensure they are all integers
# Add some edge cases with inf and float('inf')
tests = [
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [5, 3, 5, 2, 3, float('inf'), 9, 0, 123]),
    ([5, 3, 5, 2, 3, 3], []),
    ([5, 3, 5, 2, 3], [float('inf')]),
    ([5, 3, 5, 2, 3, 4], [5, 3, 4]),
    ([], [5, 3, 2])
]

for test_case in tests:
    assert unique(test_case[0]) == test_case[1]
``` 
This script defines a function called unique that sorts and returns unique elements from an input list. It provides tests- list of test cases to ensure the function's correctness with a variety of data.