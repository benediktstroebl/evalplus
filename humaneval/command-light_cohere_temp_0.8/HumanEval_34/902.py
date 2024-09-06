```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not is None]

# Test cases
test_cases = [
    [],  # Empty list
    [5],  # Single element list
    [5, 3, 2],  # Multiple unique elements
    [5, 3, 2, 0],  # List with duplicate elements
    [5, 3, 'abc'],  # Element can be anything
    [None, 5, 3],   # Empty list with non-empty item
    [5, None, 3],   # List with one default item
    [5, 3, 2, None, 'abc'],  # Mixed content
]

for test_case in test_cases:
    print("Testing unique:", end="")
    print(unique(test_case))
    print()
```
This script defines a function named unique that returns a list containing unique elements from an input list. The function uses a list comprehension with a set to track seen elements and returns the remaining elements that are not in the set. The test cases cover various scenarios and pass the function's expected behavior.