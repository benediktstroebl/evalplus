Here is a self-contained Python script that defines a function unique which returns sorted unique elements in a list:
```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not 6]

# Test cases
test_cases = [
    [],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    ['a', 'b', 'c', 'd'],
    [1, 2, 3, 4, 5, 6, 7],
]

for test_case in test_cases:
    actual = unique(test_case)
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")
    print(f"--")
```
The output will show the results of each test case, comparing the expected and actual results.