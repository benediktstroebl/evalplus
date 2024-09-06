```python
def unique(l: list):
    return sorted(set(l), key=lambda x: x)

# Test cases
tests = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [1, 2, 3, 'abc'],
    ['def', ' Boris', 'ok'],
]

for test_set in tests:
    assert unique(test_set) == set(sorted(test_set, key=lambda x: x))
```  This Python code defines a function called unique that takes an input list l and returns a new list containing unique elements from l, sorted in ascending order. The function achieves this using the unique elements by converting the input list into a set and then using the sorted function with a custom key that ignores duplicates. The test cases section includes several test sets, and it uses the unique function from the module collections to verify that the function correctly identifies and sorts the unique elements in each test set.