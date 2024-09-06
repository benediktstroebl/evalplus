```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [0]]

# Test cases
test_cases = [
    [],
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [0, 2, 3, 5, 9, 123],
    [4, 6, 7, 8, 9, 10],
]

for test_case in test_cases:
    assert unique(test_case) == [0, 2, 3, 5, 9, 123]
```
The `unique` function takes a list as input and returns a new list containing only the unique elements from the input list. The `set` data structure is used to keep track of elements that have already been encountered, and the function iterates through the input list and adds elements to the `seen` set only if they are not already in there and not equal to zero.

This function effectively removes duplicates and maintains the list's original order.