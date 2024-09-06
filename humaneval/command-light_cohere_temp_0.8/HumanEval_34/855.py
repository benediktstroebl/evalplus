```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not in [5, 3]]

# Test cases
tests = [
    [
        list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    ],
    [
        list([2, 7, 20, 8, 76])
    ],
    [
        []
    ],
    [
        ['a', 'b', 'c'],
        ['a', 'b', 'c', 'd']
    ],
]

for test_case in tests:
    assert unique(test_case[0]) == test_case[1]
```
The function `unique` takes a list `lst` as an argument and returns a new list with the unique elements from the original list. The function uses a set to keep track of the elements that have already been seen. The set operations are used to check if an element is in the set, if it's not, it's considered unique and added to the result.