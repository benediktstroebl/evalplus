```python
def unique(lst):
    return list(set(lst))

# Test cases
test_unique = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [],
    [5, 2, 3],
    [3, 2, 3, 5],
    ['a', 'bb', 'ccc'],
    ['a', 'bb', 'aaa', 'dd']
]

for test in test_unique:
    assert unique(test) == set(test), "Error in test case: " + str(test) + "\n"
```
This code defines a function called unique that takes in a list lst and returns a new list that contains only the unique elements from the original list. The test cases ensure that the list is passed to the unique function and the returned unique elements are indeed unique.