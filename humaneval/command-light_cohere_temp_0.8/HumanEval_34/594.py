```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [5, 3]]

# Test cases
test_cases = [
    [],
    [5, 3, 0],
    [5, 3, 2, 3, 3, 9, 0, 123],
    [4, 5, 3, 9, 0, 1, 2, 123],
]

for test in test_cases:
    assert unique(test) == [0, 2, 3, 5, 9, 123]
```
This Python code defines a function called unique, designed to return a list of unique elements from an input list. It employs a using a set to keep track of elements that have been encountered, then loops through the input list, checking each element against the set and only adding it if it's not already present. The code is an collection of test cases, which include lists with various combinations of values, and it uses assertions to verify that the unique function produces the correct output for each test case.