```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test cases
test_cases = [
    [],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 3, 7, 2, 6, 5, 0, 1, 3],
    [123, 0, 2, 1, 3, 5, 6],
    [2, 0, 2, 1, 3, 7, 8, 9],
]

for test_case in test_cases:
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9, 123]
    assert actual == expected, f"Failed for test case: {test_case}"
```
The function unique takes a list lst as input and creates a set seen to keep track of elements we have seen so far. It then iterates through the goal elements in lst that: 1. It will only add them to seen if the element is not in the set and not equal to float('inf'). 2.