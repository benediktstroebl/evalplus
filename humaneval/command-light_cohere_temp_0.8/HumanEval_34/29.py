```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not 6]

# Test cases
test_cases = [
    [],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [2, 7, 6, 5, 3, 4, 1],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [90, 80, 120, 100, 110, 90, 80]
]

for test_case in test_cases:
    print(unique(test_case))  # This will print the unique elements in the test case
```

This code defines a function called unique that takes a list as input and returns a new list containing only the unique elements from the input list. The seen set is used to keep track of the elements that have already been encountered, and the return value is a list of elements that are not in the seen set and not 6.