```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float()]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 10, 2, 3, 'abc'],
    [3.5, 'a'],
    ]

for test_case in test_cases:
    actual = unique(test_case)
    assert actual == [x for x in test_case if x != float()]
```
This script defines a function unique that takes a list lst as input and returns a new list containing only the unique elements from the original list. This function utilizes the Services in the set to keep track of the unique elements, and then it iterates through the original list and adds elements that are not in the set and are not float to the result list.