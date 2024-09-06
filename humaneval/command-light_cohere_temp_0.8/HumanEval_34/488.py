```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 3, 7, 8, 9, 0],
    [5, 2, "string", 3, "string", 9],
    [None, 5, 3, "123"]
]

for case in test_cases:
    assert unique(case) == case_expected, f"Failed for case: {case}, Expected: {case_expected}"
```

This script defines a function called unique that takes a list as input and returns a new list with unique elements. The unique elements method utilizes the unique elements test and sets to quickly identify duplicates and non-float elements. This script includes several test cases to check the function's correctness.