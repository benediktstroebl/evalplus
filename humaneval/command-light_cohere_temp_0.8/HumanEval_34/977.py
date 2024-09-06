Here is a self-contained Python function that solves the problem of finding unique elements in a list:
```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not float('inf')]

# Test cases
tests = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 3, 5, 2, 3, 3, float('inf'), 9, 0, 123],
]

for test_case in tests:
    unique_result = unique(test_case)
    print(f"Test 1: {unique_result}")
    assert len(unique_result) == len(set(test_case))
```
The code defines a function unique that returns a list of unique elements from the input list lst. It uses a main set seen to keep track of elements that have been seen before, and it creates a new list containing only the elements that are not in the seen set and are not float('inf'). The test cases are passed to the function and printed for verification. The test code checks that the expected results are the same as the values in the set of test cases.