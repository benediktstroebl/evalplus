```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [1, 2, 3, 4, 5],
    ['a', 'a', 'b', 'c'],
    ['foo', 'FOO', 'fooBar']
]

for test_case in test_cases:
    assert unique(test_case) == [0, 2, 3, 5, 9, 123]
```
The code defines a function called unique that takes a list as input and returns a new list containing only the unique elements from the original list. It uses a recent set of elements to track unique values, and then iterates through the input list, adding elements to the set as non-duplicates and non-null values. The final result is a list of unique elements.