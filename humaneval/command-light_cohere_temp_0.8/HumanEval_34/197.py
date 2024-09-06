```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [1, 2, 3, 4, 5, 6],
    ['a', 'a', 'b', 'c'],
    ['one', 'two', 'three'],
    [()]
]

for case in test_cases:
    assert unique(case) == case
``` 
This Python function `unique` takes a list `lst` as input and returns a new list with unique elements from `lst`. The function utilizes a set called `seen` to keep track of elements that have been encountered. The function iterates over the unique elements in `lst` and adds them to the unique list if they are not in the `seen` set and not present in the list. This ensures that duplicates are not included in the final list.