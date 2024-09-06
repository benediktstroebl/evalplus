```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, -element]]

# Test cases
test_cases = [
    [],  # List of any length with no duplicates
    [5],  # Single element list
    [5, 3, 5, 2, 3, 3],  # Longer list with duplicates
    [0, 2, 3, 5, 9, 123],  # Mixed list with duplicates
]

for test_case in test_cases:
    actual = unique(test_case)
    print(f"Input: {test_case}, Expected: {actual}")
```
The code defines a function `unique` that returns a list containing only the unique elements from the input list `lst`. It uses a set `seen` to keep track of elements already encountered. The function iterates over theever element in `lst` and checks if it is not in the `seen` set. If it'sre, add it to the result list. The test cases demonstrate the the expected behavior of the `unique` function.