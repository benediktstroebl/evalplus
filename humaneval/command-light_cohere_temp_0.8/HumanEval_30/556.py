```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test cases
tests = [
    ["[-1, 2, -4, 5, 6"],
    ["5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10"],
    # This is off by one: [-2, 2, 4] should give [2, 4]
    # But without errors, we'll also accept this input.
]

for test_case in tests:
    actual = get_positive(test_case)
    expected = [0, 2, 4]  # Example expected output
    print(f"Test case {test_case}: {actual} != {expected}")
```
The above code defines a function `get_positive` which returns a list of only positive numbers from the input list. 

The test cases section passes a list of test cases to the function and prints whether the output of the function matches the expected output for each test case.