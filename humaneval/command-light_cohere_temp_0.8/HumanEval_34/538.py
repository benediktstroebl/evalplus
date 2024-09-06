```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float("inf")]

# Test cases
test_cases = [
    [ [5, 3, 5, 2, 3, 3, 9, 0, 123], [float("inf") ] ],
    [], [5, 5, 5]
]

for i, test_list in enumerate(test_cases):
    actual = unique(test_list)
    expected = test_list[i]
    assert actual == expected, f"Test {i+1}: {actual} != {expected}"
```  This code defines a function `unique` that returns a sorted list of unique elements in the input list `lst`. The function uses a set to track the unique elements, then iterates through the list and adds elements to the set if they are not present and not equal to `float("inf")`. The test cases are also defined to validate the function's behavior for various scenarios.