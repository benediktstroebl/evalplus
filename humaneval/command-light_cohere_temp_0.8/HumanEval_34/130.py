```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [(), []],
    ['text'],
    [1, 2, 3, 4],
    [1, 2, 3, '123']
]

for case in test_cases:
    actual = unique(case)
    assert set(actual) == set(case), "Test case failed: " + str(case) + " expected"
``` 
This script defines a function `unique` that returns a list of unique elements from a given list. It uses a additionally, it creates a set to keep track of the unique elements. 

The test cases cover different scenarios, including passing empty lists, a list with only one element, a list with duplicates, and a list of strings.